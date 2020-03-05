import os
import logging

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
        resp_json_payload = response.json()
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    except:
        error_msg = 'Google maps cannot find your address or API connection is not active'
        return error_msg

    address_coordinates = lat, lng

    return address_coordinates


if __name__ == '__main__':
    pass
