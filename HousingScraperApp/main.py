"""
Run main application logic here

"""

# Import the necessary modules

from utils.ingestion import scraper, url_builder, storage
from utils.ingestion import run_tracker


def app():

    # Get the latest run_id
    latest_run_id = run_tracker.get_latest_run_id(parquet_dir="./data/raw", filename="scraped_html")
    print('Building URL...')
    url = url_builder.build_url()
    print(f'Scraping from URL: {url}')
    html_string, scraped_at = scraper.scrape(url=url)
    print('Appending to Parquet...')
    storage.append_to_parquet(run_id=latest_run_id
                              , url=url
                              , scraped_data=html_string
                              , filename="scraped_html"
                              , timestamp=scraped_at
                              , query_params = url.split("?")[1]
                              )



if __name__ == "__main__":
    app()