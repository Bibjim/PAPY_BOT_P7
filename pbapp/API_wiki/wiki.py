# -*- coding: utf-8 -*-

import requests


class Wiki:
    """
    Method for finding an article on the Wikipedia API with the GPS data returned by the Google API according to the
     user request

     Input parameter to search for the page according to user request: 'Lat' and 'lng'
     Return: the page id according to the defined parameters and the user request

     Input parameter for article search: page id
     Return: the article according to the defined parameters and the page id
    """
    def __init__(self):
        """Initialize Wikipedia API url"""
        self.url = "https://fr.wikipedia.org/w/api.php"

    def get_page_id_wiki(self, lat, lng):
        """Method for finding the page id according to GPS coordinates"""
        param_lat_lng = "|".join([str(lat), str(lng)])
        params = {
            'action': 'query',
            'list': 'geosearch',
            'gsradius': 10000,
            'gscoord': param_lat_lng,
            'format': 'json',
        }
        # Method get to find the id according to the parameters defined in the API
        return_id = requests.get(self.url, params=params)
        page_id = return_id.json()['query']['geosearch'][0]['pageid']
        print("Id : ", page_id)
        return page_id

    def get_article_wiki(self, page_id):
        """Method for finding the article according to page id"""
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "indexpageids": 1,
            "exsentences": "5",
            "pageids": page_id,
        }
        # Method get to find the article according to the parameters defined in the API
        resp = requests.get(self.url, params=params)
        resp = resp.json()
        content_wiki = resp['query']['pages'][str(page_id)]['extract']
        print("wiki : ", content_wiki)
        return content_wiki
