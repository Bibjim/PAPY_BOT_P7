# -*- coding: utf-8 -*-

import os

import requests


def get_address_gmaps(address: str) -> dict:
    """
    Connection to the Google maps API
    Conversion of the data '#nameInput' to GPS coordinate
    :param address: data request AJAX with flask method 'POST'
    :return: coordinates
    """
    apiKey = os.getenv("API_KEY")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ', '+'), apiKey))
    try:
        response = requests.get(url)
        # print(response)
        resp_json = response.json()
        # print(resp_json)
        lat = resp_json['results'][0]['geometry']['location']['lat']
        lng = resp_json['results'][0]['geometry']['location']['lng']
    except:
        error_msg = 'Google maps ne trouve pas les coordonnées GPS' \
                    'ou la connexion à l\'API ne fonctionne pas'
        return error_msg

    address_coordinates = {'lat': lat, 'lng': lng}
    # print(address_coordinates)

    return address_coordinates


if __name__ == '__main__':
    pass
