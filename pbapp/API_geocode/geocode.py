# -*- coding: utf-8 -*-

import os
import geocoder


class GeoMaps:

    def __init__(self):
        # self.apikey = os.getenv("API_KEY")
        self.apikey = "AIzaSyDeT-agUpv_TLsOvRo3HxKSLaJd2WCdp1U"

    def get_address_gmaps(self, adress):
        response = geocoder.google(adress, key=self.apikey)
        if response.ok:
            resp_json = response.json
            lat = resp_json["lat"]
            lng = resp_json["lng"]
            print("lat : ", lat)
            print("lng : ", lng)
            return lat, lng
        else:
            return None

