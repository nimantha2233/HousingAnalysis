"""
Run main application logic here

"""

# Import the necessary modules

from utils.ingestion import scraper, url_builder, storage
from utils.ingestion import run_tracker
import logging
from logging.handlers import RotatingFileHandler


# Set up rotating file handler (5MB max per file, keep last 3 logs)
log_handler = RotatingFileHandler("logs/app.log", maxBytes=5_000_000, backupCount=3)
# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Default log level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("./logs/app.log"),  # Save logs to a file
        logging.StreamHandler()  # Show logs in the console
    ]
)

logger = logging.getLogger(__name__)  # Get logger for this file


def app():

    logger.info("Starting the application")
    # Get the latest run_id
    latest_run_id = run_tracker.get_latest_run_id(parquet_dir="./data/raw", filename="scraped_html")
    # build URL using defined params
    url = url_builder.build_url()
    # Scrape the HTML content of the page
    html_string, scraped_at = scraper.scrape(url=url)
    # Append the scraped data to the Parquet file
    storage.append_to_parquet(run_id=latest_run_id
                              , url=url
                              , scraped_data=html_string
                              , filename="scraped_html"
                              , timestamp=scraped_at
                              , query_params = url.split("?")[1]
                              )



if __name__ == "__main__":
    app()