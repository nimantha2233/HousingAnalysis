""""""
import polars as pl
from pathlib import Path

def append_to_parquet(run_id, url : str, scraped_data : str, filename : str, timestamp : str, query_params : str):
    """Append new weekly scraped data to an existing Parquet file."""

    filepath = f'./data/raw/{filename}'
    if Path(filepath).exists():
        existing_df = pl.read_parquet(filepath)  # Load existing data
        df = pl.concat([existing_df, pl.DataFrame({'run_id': run_id
                                                    , 'scrape_datetime' : timestamp
                                                    , 'url' : url
                                                    , 'html_string' : scraped_data
                                                    , 'query_params' : query_params
                                                    }
                                                )])
    else:
        print("⚠ File not found. Creating a new Parquet file...")
        df = pl.DataFrame(pl.DataFrame({'run_id': run_id
                                        , 'scrape_datetime' : timestamp
                                        , 'url' : url
                                        , 'html_string' : scraped_data
                                        , 'query_params' : query_params
                                        }
                                        ))
    # write/re-write the parquet file
    df.write_parquet(filepath)



    
