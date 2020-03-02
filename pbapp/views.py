import requests

from flask import Flask, render_template, url_for, jsonify, request

from config import API_Key

app = Flask(__name__)
apiKey = API_Key


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajax', methods=['GET', 'POST'])
def process():
    name = request.form['name']

    if name:
        address = str(name)
        url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
               .format(address.replace(' ', '+'), apiKey))
        try:
            response = requests.get(url)
            resp_json_payload = response.json()
            lat = resp_json_payload['results'][0]['geometry']['location']['lat']
            lng = resp_json_payload['results'][0]['geometry']['location']['lng']
        except:
            print('ERROR: {}'.format(address))
            lat = 0
            lng = 0
        lat = lat
        lng = lng
        coordinates = lat, lng

        return jsonify({'name': coordinates})

    return jsonify({'error': 'error name'})
