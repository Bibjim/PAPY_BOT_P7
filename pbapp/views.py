# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, url_for, jsonify, request

from pbapp.API_geocode import GeoMaps
from pbapp.API_wiki import Wiki

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/ajax", methods=["POST"])
def process():
    query = request.form["query"]
    rep = GeoMaps()
    coords = rep.get_address_gmaps(query)
    if coords is not None:
        wiki = Wiki()
        page_id = wiki.get_page_id_wiki(coords[0], coords[1])
        article = wiki.get_article_wiki(page_id)
        return jsonify({"lat": coords[0], "lng": coords[1], "content": article})

    else:
        print("Je n'ai pas trouvé la recherche")
