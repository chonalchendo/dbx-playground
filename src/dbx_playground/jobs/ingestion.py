#!/usr/bin/env python3
"""Data ingestion job for streaming files to Delta tables."""

import sys
import typing as T

import rich
from loguru import logger
from pydantic import ValidationError
from pyspark.sql import SparkSession

import dbx_playground.args as args
import dbx_playground.configs as configs
import dbx_playground.jobs.base as base


class IngestionJob(base.Job):
    """Streams data from cloud storage to Delta tables."""

    KIND: T.Literal["IngestionJob"] = "IngestionJob"
    path: str
    format: str
    schema: str
    table: str
    mode: str = "append"

    @T.override
    def run(self) -> base.Locals:
        """Execute the ingestion job."""
        logger.info("Initializing Spark Session")
        spark = SparkSession.builder.appName("S3ToBronze").getOrCreate()

        logger.info(f"Reading file: {self.path}")
        df = (
            spark.readStream.format("cloudFiles")
            .option("cloudFiles.format", self.format)
            .load(self.path)
        )

        logger.info(f"Writing to table: {self.schema}.{self.table}")
        checkpoint_path = f"/mnt/{self.schema}/_checkpoints/{self.table}"

        (
            df.writeStream.format("delta")
            .option("checkpointLocation", checkpoint_path)
            .outputMode(self.mode)  # Fixed: was self.append
            .table(f"{self.schema}.{self.table}")
        )


def main() -> int:
    """Main entry point for the ingestion job."""
    try:
        # Parse arguments
        args_ = args.parse_job_args(description="Run DBX Ingestion Job")

        # Load and merge configuration
        logger.info(f"Loading configuration from: {args_.config}")
        merged_config = configs.load_and_merge_configs([args_.config], args.extras)
        config_object = configs.to_object(merged_config)

        rich.print("[bold blue]Configuration:[/bold blue]")
        rich.print(config_object)

        # Validate and create job
        job = IngestionJob.model_validate(config_object)

        # Run the job
        logger.info("Starting ingestion job")
        job.run()
        logger.success("Job completed successfully")

        return 0

    except FileNotFoundError as e:
        logger.error(f"Configuration file not found: {e}")
        return 1

    except ValidationError as e:
        logger.error("Configuration validation failed")
        rich.print(e)
        return 1

    except Exception as e:
        logger.exception(f"Job failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
