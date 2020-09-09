import requests
from math import *

URL = "https://api.postcodes.io/postcodes/"


def lon_lat(postcode):
    r = requests.get(url=URL + postcode)
    data = r.json()
    return data["result"]["latitude"], data["result"]["longitude"]


def haversin(x):
    return sin(x / 2) ** 2


def great_circle_distance(loc1, loc2):
    lat1, lon1 = loc1
    lat2, lon2 = loc2
    return 2 * asin(sqrt(haversin(lat2 - lat1) + cos(lat1) * cos(lat2) * haversin(lon2 - lon1)))


locale1 = lon_lat("E6 3SQ")
locale2 = lon_lat("E1 0LB")

ang_distance = great_circle_distance(locale1, locale2)
# - Convert to km
