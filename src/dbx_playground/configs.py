import os
import typing as T
from pathlib import Path

import omegaconf as oc

type Config = oc.ListConfig | oc.DictConfig
type Configs = T.Sequence[Config]


def get_repo_root() -> Path:
    """Get the repository root directory.

    In Databricks, this resolves from the script location.
    Locally, uses the current working directory.

    Returns:
        Path: The repository root directory.
    """
    if "DATABRICKS_RUNTIME_VERSION" in os.environ:
        # In Databricks, calculate from this file's location
        # This file is at: src/dbx_playground/configs.py
        this_file = Path(__file__).resolve()
        # Go up: configs.py -> dbx_playground -> src -> repo_root
        return this_file.parent.parent.parent
    else:
        # Local development - use current working directory
        return Path.cwd()


def resolve_config_path(config_path: str | Path) -> Path:
    """Resolve a config path relative to the repository root.

    Args:
        config_path: Relative path to config file from repo root.

    Returns:
        Path: Absolute path to the config file.
    """
    repo_root = get_repo_root()
    resolved_path = repo_root / config_path

    if not resolved_path.exists():
        raise FileNotFoundError(
            f"Config file not found: {resolved_path}\n"
            f"Repository root: {repo_root}\n"
            f"Relative path: {config_path}"
        )

    return resolved_path


def parse_file(path: str | Path) -> Config:
    """Parse a config file from a path.

    Args:
        path: Path to config file (relative to repo root or absolute).

    Returns:
        Config: Representation of the config file.
    """
    # Resolve the path if it's relative
    path_obj = Path(path)
    if not path_obj.is_absolute():
        path_obj = resolve_config_path(path)

    return oc.OmegaConf.load(str(path_obj))


def parse_string(string: str) -> Config:
    """Parse the given config string.

    Args:
        string: Content of config string.

    Returns:
        Config: Representation of the config string.
    """
    return oc.OmegaConf.create(string)


def merge_configs(configs: Configs) -> Config:
    """Merge a list of config into a single config.

    Args:
        configs: List of configs.

    Returns:
        Config: Representation of the merged config objects.
    """
    return oc.OmegaConf.merge(*configs)


def to_object(config: Config, resolve: bool = True) -> object:
    """Convert a config object to a python object.

    Args:
        config: Representation of the config.
        resolve: Resolve variables. Defaults to True.

    Returns:
        object: Conversion of the config to a python object.
    """
    return oc.OmegaConf.to_container(config, resolve=resolve)


def load_and_merge_configs(
    config_files: T.Sequence[str | Path],
    extras: T.Sequence[str] | None = None,
) -> oc.DictConfig:
    """Load configuration files and merge with extra parameters.

    Args:
        config_files: Sequence of config file paths (relative to repo root).
        extras: Optional sequence of config strings to merge.

    Returns:
        oc.DictConfig: Merged configuration.
    """
    # Parse config files (parse_file now handles path resolution)
    file_configs = [parse_file(file) for file in config_files]

    # Parse extra strings
    string_configs = []
    if extras:
        string_configs = [parse_string(string) for string in extras]

    # Merge all configs
    config = merge_configs([*file_configs, *string_configs])

    if not isinstance(config, oc.DictConfig):
        raise RuntimeError("Config is not a dictionary")

    return config
