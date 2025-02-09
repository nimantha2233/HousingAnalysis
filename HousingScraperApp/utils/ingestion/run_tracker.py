"""Utility functions for tracking the most recent run_id from Parquet files."""
import polars as pl
from pathlib import Path
import logging

# Logger specific to this module
logger = logging.getLogger(__name__)  


def get_latest_run_id(parquet_dir : str, filename : str) -> str:
    """Find the most recent run_id from existing Parquet files."""
    parquet_files = list(Path(parquet_dir).glob(f"{filename}"))
    
    if not parquet_files:
        logger.info("⚠ No Parquet files found!")
        return 1

    # Read all Parquet files and get the most recent run_id
    latest_run_id = None
    latest_timestamp = None

    for file in parquet_files:
        df = pl.read_parquet(str(file))
        if "run_id" in df.columns and "scrape_datetime" in df.columns:
            df = df.sort("scrape_datetime", descending=True)
            if latest_timestamp is None or df["scrape_datetime"][0] > latest_timestamp:
                latest_timestamp = df["scrape_datetime"][0]
                latest_run_id = df["run_id"][0]
    logger.info('Latest run_id:', latest_run_id)

    return latest_run_id + 1