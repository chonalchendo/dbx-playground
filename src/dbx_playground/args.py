"""Command-line interface utilities for DBX Playground jobs."""

import argparse
from pathlib import Path


def create_job_parser(description: str = "Run DBX job") -> argparse.ArgumentParser:
    """Create a standard argument parser for DBX jobs.

    Args:
        description: Description for the parser help text

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Path to configuration file",
    )

    parser.add_argument(
        "--extra",
        "-e",
        action="append",
        dest="extras",
        default=[],
        help="Configuration overrides in key=value format (repeatable)",
    )

    return parser


def parse_job_args(description: str = "Run DBX job") -> argparse.Namespace:
    """Parse standard job arguments from command line.

    Args:
        description: Description for the parser help text

    Returns:
        Parsed arguments namespace
    """
    parser = create_job_parser(description)
    return parser.parse_args()


def add_common_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Add common arguments to an existing parser.

    Useful when you need custom arguments plus the standard ones.

    Args:
        parser: Existing ArgumentParser instance

    Returns:
        Parser with common arguments added
    """
    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Path to configuration file",
    )

    parser.add_argument(
        "--extra",
        "-e",
        action="append",
        dest="extras",
        default=[],
        help="Configuration overrides in key=value format (repeatable)",
    )

    return parser
