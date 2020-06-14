# -*- coding: utf-8 -*-
import os
import geocoder


class GeoMaps:
    """
    Searching for GPS coordinates using the 'geocoder' framework
     Input parameter: POST request ajax method -> adress
     Parser: adress_clean
     Returns: 'lat' and 'lng'
     Purpose: display of GPS coordinates on the map and for Wikipedia research
     Note: the 'geocoder' framework also parses the input parameter
    """

    def __init__(self):
        """Initializes the Google API key"""
        self.apikey = os.getenv("API_KEY")

    def get_address_gmaps(self, adress):
        """Search method and GPS coordinates of the input parameter"""
        # print(adress)

        # Parser for special characters
        adress_clean = adress.replace("?" or "." or "/" or "%" or
                                      "!" or "§" or "*" or "=" or
                                      "+" or ":" or ";" or "," or
                                      "@" or "#" or "&" or "²", "")
        # print(adress_clean)

        response = geocoder.google(adress_clean, key=self.apikey)
        # print(response)
        if response.ok:  # if the match between the input parameter and the API is good
            resp_json = response.json
            # look up latitude and longitude data in API response
            lat = resp_json["lat"]
            lng = resp_json["lng"]
            print("lat : ", lat)
            print("lng : ", lng)
            return lat, lng  # returns the GPS data for display on the map and Wikipedia search
        else:
            return None  # if the match between the input parameter and the API is bad
