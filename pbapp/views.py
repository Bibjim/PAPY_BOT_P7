from flask import Flask, render_template, url_for, jsonify, request

from pbapp.API_geocode.geocode import get_address_gmaps

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajax', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    if request.method == "POST":
        results = get_address_gmaps(address=name)
        print(results)

        return jsonify(results)
