import sys
import typing as T
from pathlib import Path

import kaggle
import polars as pl
import rich
from dotenv import load_dotenv
from loguru import logger

import dbx_playground.args as args
import dbx_playground.configs as configs
import dbx_playground.jobs.base as base

load_dotenv()


class ExtractionJob(base.Job):
    KIND: T.Literal["ExtractionJob"] = "ExtractionJob"

    input_dataset: str
    output_path: str
    unzip: bool

    @T.override
    def run(self) -> base.Locals:
        logger.info("Authenticating Kaggle API")
        kaggle.api.authenticate()

        output_dir = Path(self.output_path).parent

        logger.info("Creating Tmp folder")
        tmp_folder = Path("tmp")
        tmp_folder.mkdir(exist_ok=True)

        if "s3" not in self.output_path:
            logger.info(f"Creating output directory: {output_dir}")
            output_dir.mkdir(exist_ok=True, parents=True)

        logger.info(f"Downloading dataset: {self.input_dataset}")
        kaggle.api.dataset_download_files(
            dataset=self.input_dataset, path=tmp_folder, unzip=self.unzip
        )

        paths = Path("tmp").glob("*.csv")

        datasets = []
        for path in paths:
            if not Path(path).exists():
                logger.error(f"Data did not download correctly: {path}")
                raise FileNotFoundError(f"Data did not download correctly: {path}")

            data = pl.read_csv(path)
            # delete original csv files
            path.unlink()
            datasets.append(data)

        # delete tmp folder
        tmp_folder.rmdir()

        # concat datasets together
        df: pl.DataFrame = pl.concat(datasets, how="vertical_relaxed")

        logger.info(f"Writing dataset to path: {self.output_path}")
        df.write_parquet(self.output_path)

        return locals()


def main() -> int:
    """Main entry point for the ingestion job."""
    # Parse arguments
    args_ = args.parse_job_args(description="Run DBX Ingestion Job")

    # Load and merge configuration
    logger.info(f"Loading configuration from: {args_.config}")
    merged_config = configs.load_and_merge_configs([args_.config], args_.extras)
    config_object = configs.to_object(merged_config)

    rich.print("[bold blue]Configuration:[/bold blue]")
    rich.print(config_object)

    # Validate and create job
    job = ExtractionJob.model_validate(config_object)

    # Run the job
    logger.info("Starting ingestion job")
    job.run()
    logger.success("Successfully completed ExtractionJob")

    return 0


if __name__ == "__main__":
    sys.exit(main())
