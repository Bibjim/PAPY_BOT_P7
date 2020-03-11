# -*- coding: utf-8 -*-

import requests
from typing import Union

url = "https://fr.wikipedia.org/w/api.php"


def get_id_wiki(lat: Union[int, float], lng: Union[int, float]) -> int:
    params = {
        'action': 'query',
        'list': 'geosearch',
        'gsradius': 10000,
        'gscoord': f'{lat}|{lng}',
        'format': 'json',
        'formatversion': 2
    }
    try:
        return_id = requests.get(url, params=params)
        wiki_id = return_id.json()['query']['geosearch'][0]['pageid']
    except:
        error_msg = 'Je n\'ai pas trouvé la page wiki'
        return error_msg

    page_id = wiki_id
    return page_id


def get_article_wiki(page_id: int) -> dict:
    params = {
        'action': 'query',
        'prop': 'info|extracts|pageimages',
        'inprop': 'url',
        'explaintext': '',
        'exintro': 1,
        'exsectionformat': 'plain',
        'format': 'json',
        'formatversion': 2,
        'pageids': page_id,
        'pithumbsize': 500
    }
    try:
        resp = requests.get(url, params=params)
        resp = resp.json()
        content_wiki = resp['query']['pages'][0]['extract']
        thumbnail_wiki = resp['query']['pages'][0]['thumbnail']['source']
    except:
        error_msg = 'Je n\'ai pas compris votre question'
        return error_msg

    wiki_article = {
        'content': content_wiki,
        'thumbnail': thumbnail_wiki
    }
    return wiki_article
