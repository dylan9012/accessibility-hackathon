import requests
from math import *

URL = "https://api.postcodes.io/postcodes/"
R = 6370.0 # - Earth's radius in km'

def lon_lat(postcode):
	r = requests.get(url=URL + postcode)
	data = r.json()
	return radians(data["result"]["latitude"]), radians(data["result"]["longitude"])

def great_circle_distance(loc1, loc2):
	lat1, lon1 = loc1
	lat2, lon2 = loc2
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	return 2 * atan2(sqrt(a), sqrt(1 - a))


locale1 = lon_lat("E6 3SQ")
locale2 = lon_lat("E1 0LB")

ang_distance = great_circle_distance(locale1, locale2)
print("{:.1f}km away".format(ang_distance*R))
