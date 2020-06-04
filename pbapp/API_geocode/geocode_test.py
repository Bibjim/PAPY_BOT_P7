# -*- coding: utf-8 -*-

import requests
from json import loads

from pbapp.API_geocode.geocode import *


def test_coords(monkeypatch):
    def fake_coords(url, address):
        class FakeResponse():
            def json():
                results = {'lat': 48.856614, 'lng': 2.3522219}
                return results

        return FakeResponse

    monkeypatch.setattr(requests, 'get', fake_coords)
    address_coordinates = get_address_gmaps(address='paris')
    assert address_coordinates == {'lat': 48.856614, 'lng': 2.3522219}
