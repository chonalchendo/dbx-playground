#!/usr/bin/env python3
"""Data ingestion job for streaming files to Delta tables."""

import sys
import typing as T

import rich
from databricks.sdk.runtime import dbutils
from loguru import logger
from pydantic import ValidationError
from pyspark.sql import SparkSession

import dbx_playground.args as args
import dbx_playground.configs as configs
import dbx_playground.jobs.base as base


class IngestionJob(base.Job):
    """Streams data from cloud storage to Delta tables."""

    KIND: T.Literal["IngestionJob"] = "IngestionJob"
    spark_app_name: str
    input_path: str
    input_format: str
    output_schema: str
    output_table: str
    mode: str

    @T.override
    def run(self) -> base.Locals:
        """Execute the ingestion job."""
        logger.info("Initializing Spark Session")
        spark = SparkSession.builder.appName(self.spark_app_name).getOrCreate()

        # Configure S3 access using secrets
        access_key = dbutils.secrets.get(scope="aws", key="aws-access-key-id")
        secret_key = dbutils.secrets.get(scope="aws", key="aws-secret-access-key")

        spark.conf.set("fs.s3a.access.key", access_key)
        spark.conf.set("fs.s3a.secret.key", secret_key)

        logger.info(f"Reading file: {self.input_path}")
        df = (
            spark.readStream.format("cloudFiles")
            .option("cloudFiles.format", self.input_format)
            .load(self.input_path)
        )

        logger.info(f"Writing to table: {self.output_schema}.{self.output_table}")
        checkpoint_path = f"/mnt/{self.output_schema}/_checkpoints/{self.output_table}"

        (
            df.writeStream.format("delta")
            .option("checkpointLocation", checkpoint_path)
            .outputMode(self.mode)  # Fixed: was self.append
            .table(f"{self.output_schema}.{self.output_table}")
        )


def main() -> int:
    """Main entry point for the ingestion job."""
    try:
        # Parse arguments
        args_ = args.parse_job_args(description="Run DBX Ingestion Job")

        # Load and merge configuration
        logger.info(f"Loading configuration from: {args_.config}")
        merged_config = configs.load_and_merge_configs([args_.config], args_.extras)
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
