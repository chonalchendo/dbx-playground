import typing as T
from pathlib import Path

import kaggle
import polars as pl
from dotenv import load_dotenv
from loguru import logger

import dbx_playground.jobs.base as base

load_dotenv()


class ExtractionJob(base.Job):
    KIND: T.Literal["ExtractionJob"] = "ExtractionJob"

    path: str
    dataset: str
    unzip: bool

    @T.override
    def run(self) -> base.Locals:
        logger.info("Authenticating Kaggle API")
        kaggle.api.authenticate()

        output_dir = Path(self.path).parent

        logger.info("Creating Tmp folder")
        tmp_folder = Path("tmp")
        tmp_folder.mkdir(exist_ok=True)

        if "s3" not in self.path:
            logger.info(f"Creating output directory: {output_dir}")
            output_dir.mkdir(exist_ok=True, parents=True)

        logger.info(f"Downloading dataset: {self.dataset}")
        kaggle.api.dataset_download_files(
            dataset=self.dataset, path=tmp_folder, unzip=self.unzip
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

        logger.info(f"Writing dataset to path: {self.path}")
        df.write_parquet(self.path)

        logger.success("Successfully completed ExtractionJob")
        return locals()
