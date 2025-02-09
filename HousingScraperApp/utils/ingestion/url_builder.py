# Define the parameters
"""
This module constructs a URL for querying property listings from Rightmove based on specified parameters.
The parameters include:
- locationIdentifier: Identifier for the location to search within.
- maxBedrooms: Maximum number of bedrooms.
- minBedrooms: Minimum number of bedrooms.
- maxPrice: Maximum price of the property.
- radius: Search radius in miles.
- index: Index for pagination.
- propertyTypes: Types of properties to include in the search.
- includeSSTC: Whether to include properties that are Sold Subject to Contract.
- mustHave: Features that the property must have.
- dontShow: Features that the property must not have.
- furnishTypes: Types of furnishings to include in the search.
- keywords: Keywords to include in the search.
The constructed URL can be used to make a GET request to Rightmove's property search endpoint.
"""
from ..configs.url_params import params
import logging

# Logger specific to this module
logger = logging.getLogger(__name__)  



def build_url() -> str:

    logger.info("Building URL...")

    # Construct the URL using f-string
    url = (
        f"https://www.rightmove.co.uk/property-for-sale/find.html?"
        f"locationIdentifier={params['locationIdentifier']}&"
        f"maxBedrooms={params['maxBedrooms']}&"
        f"minBedrooms={params['minBedrooms']}&"
        f"maxPrice={params['maxPrice']}&"
        f"radius={params['radius']}&"
        f"index={params['index']}&"
        f"propertyTypes={params['propertyTypes']}&"
        f"includeSSTC={params['includeSSTC']}&"
        f"mustHave={params['mustHave']}&"
        f"dontShow={params['dontShow']}&"
        f"furnishTypes={params['furnishTypes']}&"
        f"keywords={params['keywords']}"
    )

    return url