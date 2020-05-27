# -*- coding: utf-8 -*-

import requests
from json import loads

from pbapp.API_geocode.geocode import *


def test_coords(monkeypatch):
    def fake_coords(url):
        class FakeResponse():
            def json():
                results = {'lat': 48.856614, 'lng': 2.3522219}
                return loads(results)

        return FakeResponse

    fake_results = {'lat': 48.856614, 'lng': 2.3522219}

    monkeypatch.setattr(requests, 'get', fake_coords)
    address_coordinates = get_address_gmaps(address='paris')
    assert address_coordinates == fake_results
