"""
Module to scrape housing data from Rightmove.

The main tasks carried out by this module:

    1. Scrape housing data from Rightmove.
    2. Write HTML data to a HTML file in LZ.
"""

import requests
from datetime import datetime

def scrape(url: str) -> str:
    """
    Params:
        url (str): The URL of the page to scrape.
    
    Returns:
        str: The HTML content of the page if the request is successful.
    
    Raises:
        Exception: If the request fails with a status code other than 200.
    """

    # Make a request to the URL
    r = requests.get(url)
    scraped_at = datetime.now().replace(microsecond=0)

    # Check the status code
    if r.status_code == 200:
        print(f"Success Accessing page, status code: {r.status_code}")
    else:
        raise Exception(f"Failed to access page, status code {r.status_code}")
    
    return r.text, scraped_at


