# -*- coding: utf-8 -*-

import os

import requests

apiKey = os.getenv("API_KEY")


def get_address_gmaps(address, apiKey):
    """
    Connection to the Google maps API
    Conversion of the data '#nameInput' to GPS coordinate
    :param address: data request AJAX with flask method 'POST'
    :return: coordinates
    """

    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address, apiKey))

    response = requests.get(url)
    # print(response)
    resp_json = response.json()
    print(resp_json)
    # lat = resp_json['results'][0]['geometry']['location']['lat']
    print(type(resp_json['results'][0]['geometry']['location']['lat']))
    # lng = resp_json['results'][0]['geometry']['location']['lng']
    print(resp_json['results'][0]['geometry']['location']['lng'])
    lat = 48.5734053
    lng = 7.752111299999999

    address_coordinates = {'lat': lat, 'lng': lng}

    print(address_coordinates)

    return address_coordinates


if __name__ == '__main__':
    pass
