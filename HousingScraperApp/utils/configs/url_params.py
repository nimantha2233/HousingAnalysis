# Define the parameters
params = {
    "locationIdentifier": "REGION^87490",
    "maxBedrooms": 3,
    "minBedrooms": 2,
    "maxPrice": 450000,
    "radius": 15.0,
    "index": 0,
    "propertyTypes": "bungalow,detached,semi-detached,terraced",
    "includeSSTC": "false",
    "mustHave": "",
    "dontShow": "newHome",
    "furnishTypes": "",
    "keywords": ""
}

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