# -*- coding: utf-8 -*-

import requests


class Wiki:
    def __init__(self):
        self.url = "https://fr.wikipedia.org/w/api.php"

    def get_page_id_wiki(self, lat, lng):
        param_lat_lng = "|".join([str(lat), str(lng)])
        params = {
            'action': 'query',
            'list': 'geosearch',
            'gsradius': 10000,
            'gscoord': param_lat_lng,
            'format': 'json',
        }

        return_id = requests.get(self.url, params=params)
        page_id = return_id.json()['query']['geosearch'][0]['pageid']
        print("Id : ", page_id)
        return page_id

    def get_article_wiki(self, id):
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "indexpageids": 1,
            "exsentences": "5",
            "pageids": id,
        }

        resp = requests.get(self.url, params=params)
        resp = resp.json()
        content_wiki = resp['query']['pages'][str(id)]['extract']
        print("wiki : ", content_wiki)
        return content_wiki
