import os
from flask import Flask, render_template, url_for, jsonify, request

from pbapp.main import main_app

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html', api_key=os.getenv("API_KEY"))


@app.route('/ajax', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    if request.method == "POST":
        results = main_app(name_input=name)
        print(results)

        return jsonify(results)

    return jsonify({'error': 'Google maps cannot find your address or API connection is not active'})
