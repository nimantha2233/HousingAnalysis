""""""
import polars as pl
from pathlib import Path
import logging

# Logger specific to this module
logger = logging.getLogger(__name__)  


def append_to_parquet(run_id, url : str, scraped_data : str, filename : str, timestamp : str, query_params : str) -> None:
    """
    Append new weekly scraped data to an existing Parquet file.

    Parameters:
        run_id (str): Unique identifier for the run.
        url (str): The URL from which the data was scraped.
        scraped_data (str): The HTML content that was scraped.
        filename (str): The name of the Parquet file to append to.
        timestamp (str): The timestamp when the data was scraped.
        query_params (str): The query parameters used during the scraping.
    Returns:
        None
    """
    # create relative path to parquet file
    filepath = f'./data/raw/{filename}'
    
    logging.info(f"Appending data to Parquet file: {filename}")
    
    if Path(filepath).exists():
        existing_df = pl.read_parquet(filepath)  # Load existing data
        logging.info("File found. Appending data...")
        df = pl.concat([existing_df, pl.DataFrame({'run_id': run_id
                                                    , 'scrape_datetime' : timestamp
                                                    , 'url' : url
                                                    , 'html_string' : scraped_data
                                                    , 'query_params' : query_params
                                                    }
                                                )])
    else:
        logging.info("⚠ File not found. Creating a new Parquet file...")
        df = pl.DataFrame(pl.DataFrame({'run_id': run_id
                                        , 'scrape_datetime' : timestamp
                                        , 'url' : url
                                        , 'html_string' : scraped_data
                                        , 'query_params' : query_params
                                        }
                                        ))
    # write/re-write the parquet file
    df.write_parquet(filepath)



    
