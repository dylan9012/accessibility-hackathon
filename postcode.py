from math import *

import requests


class GreatCircleDistance:
    __URL = "https://api.postcodes.io/postcodes/"
    __R = 6370.0  # - Earth's radius in km'

    def __init__(self, postcode1, postcode2):
        self._postcode1 = postcode1
        self._postcode2 = postcode2
        self._loc1 = self.lon_lat(postcode1)
        self._loc2 = self.lon_lat(postcode2)
        self._distance = self.calculation()

    def calculation(self):
        lat1, lon1 = self._loc1
        lat2, lon2 = self._loc2
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        return 2 * atan2(sqrt(a), sqrt(1 - a))

    @staticmethod
    def lon_lat(postcode):
        r = requests.get(url=GreatCircleDistance.__URL + postcode)
        data = r.json()
        return radians(data["result"]["latitude"]), radians(data["result"]["longitude"])

    def get_distance(self):
        return "{:.1f}".format(self._distance * GreatCircleDistance.__R)


if __name__ == "__main__":
    pass
