# -*- coding: utf-8 -*-

import requests

import os

from pbapp.API_geocode.geocode import *



def test_get_coordonnees_online():
    """Google API test online coordonnées"""
    apiKey = os.getenv("API_KEY")

    response = get_address_gmaps('Strasbourg', apiKey)
    assert response == {'lat': 48.5734053, 'lng': 7.752111299999999}


def test_get_coords(monkeypatch):
    """Test API GMAPS coordinates"""
    results_coordinates = {
        'lat': 5,
        'lng': 2
    }

    class MockRequests:
        """Mock class Requests"""

        def request_coord(self, url, apiKey):
            """Mock method get function"""
            return MockCoordResponse(200)

    class MockCoordResponse:
        def __init__(self, code):
            self.json = results_coordinates
            self.status_code = code

    monkeypatch.setattr('pbapp.API_geocode.geocode', MockRequests())
    results = get_address_gmaps('faraway')
    assert results == {'lat': 5, 'lng': 2}

