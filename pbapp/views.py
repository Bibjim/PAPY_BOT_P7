# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, url_for, jsonify, request

from pbapp.API_geocode import GeoMaps
from pbapp.API_wiki import Wiki

app = Flask(__name__)


@app.route('/')
def index():
    """Returns the index.html page and the Google API key"""
    return render_template('index.html', api_key=os.getenv("API_KEY"))


@app.route("/ajax", methods=["POST"])
def process():
    """Return of the ajax request data in the index.html page"""

    query = request.form["query"]  # Return of the user request from the ajax request
    # Execution of the GPS data search method in Google API
    response_coords = GeoMaps()
    coords = response_coords.get_address_gmaps(query)
    if coords is not None:
        # If the GPS coordinates are valid, execution of the article search method in the Wikipedia API
        wiki = Wiki()
        page_id = wiki.get_page_id_wiki(coords[0], coords[1])
        article = wiki.get_article_wiki(page_id)
        # Returns the GPS data and the article in the ajax request
        return jsonify({"lat": coords[0], "lng": coords[1], "content": article})

    else:
        # If the GSP coordinates were not found by the GeoMaps method, an error message is returned in the ajax request
        # with GPS coordinates at zero by default
        article = "Je ne trouve pas la ville, le lieu, ou l'adresse que vous m'avez demandé. Merci de bien vouloir " \
                  "renseigner une ville, un lieu ou une adresse."
        return jsonify({"lat": 0, "lng": 0, "content": article})
