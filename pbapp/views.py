from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)


# app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajax', methods=['POST'])
def process():
    name = request.form['name']

    if name:
        newName = name

        return jsonify({'name': newName})

    return jsonify({'error': 'Je suis peut-être vieux mais je ne comprend pas votre demande. '
                             'Choisissez une ville, un lieu ou une adresse avant de valider.'})
