# -*- coding: utf-8 -*-

from pbapp.API_geocode.geocode import GeoMaps


def test_get_coordonnees_online():
    """Google API test online coordonnées"""
    apimaps = GeoMaps()
    response = apimaps.get_address_gmaps('Avon 77')
    assert response == (48.404839, 2.720733)


def test_get_coords(monkeypatch):
    """Test API GMAPS coordinates"""
    results_coordinates = {
        'lat': 2.3,
        'lng': 56
    }

    class MockRequests:
        """Mock class Requests"""

        def google(self, url, key):
            """Mock method get function"""
            return MockCoordResponse(200)

    class MockCoordResponse:
        def __init__(self, code):
            self.ok = True
            self.json = results_coordinates
            self.status_code = code

    monkeypatch.setattr('pbapp.API_geocode.geocode.geocoder', MockRequests())
    apimaps = GeoMaps()
    results = apimaps.get_address_gmaps('Faraway')
    assert results == (2.3, 56)

