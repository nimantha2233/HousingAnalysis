""""""
from utils.ingestion import scraper
from datetime import datetime


def test_scraper_outputs():

    output_1, output_2 = scraper.scrape(url=r'https://www.rightmove.co.uk/')

    assert isinstance(output_1, str) and isinstance(output_2, datetime)