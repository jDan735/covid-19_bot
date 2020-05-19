import requests

def getWorld():
    return requests.get("https://data.nepalcorona.info/api/v1/world").json()

def getCountries():
    return requests.get("https://nepalcorona.info/api/v1/data/world").json()
    
def getCountriesHistory():
    return requests.get("https://data.nepalcorona.info/api/v1/world/history").json()