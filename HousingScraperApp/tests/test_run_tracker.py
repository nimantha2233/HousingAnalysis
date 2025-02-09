import polars as pl
from utils.ingestion import run_tracker


def test_run_id_retrieval():
    '''Check get_latest_run_id is correctly retriving the most recent run'''
    df = pl.read_parquet(source=r'.\data\raw\scraped_html')
    manual_latest_run_id = df.sort(by=['run_id'], descending=True).limit(1).select('run_id').to_series().item()

    func_run_id = run_tracker.get_latest_run_id(parquet_dir=r'./data/raw', filename='scraped_html')

    assert func_run_id == manual_latest_run_id + 1





