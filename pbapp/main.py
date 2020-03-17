# -*- coding: utf-8 -*-

from pbapp.API_geocode.geocode import get_address_gmaps
from pbapp.API_wiki.wiki import get_article_wiki, get_id_wiki


def main_app(name_input: str) -> dict:
    final_data = {
        'coords': None,
        'content': None,
        'thumbnail': None,
    }
    try:
        coords_adress = get_address_gmaps(name_input)

        final_data['coords'] = (coords_adress['lat'], coords_adress['lng'])

        page_id = get_id_wiki(coords_adress['lat'], coords_adress['lng'])
        wiki_article = get_article_wiki(page_id)

        final_data['content'] = wiki_article['content']
        final_data['thumbnail'] = wiki_article['thumbnail']
    except:
        error_msg = {'error': 'Je n\'ai pas compris votre question'}
        return error_msg

    return final_data
