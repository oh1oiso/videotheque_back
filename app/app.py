import os
import json
import requests
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to fetch movies from the API
def fetch_movies():
    url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1'
    headers = {
        'Authorization': 'Bearer YOUR_AUTH_TOKEN',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Route to get movies
@app.route('/get-movies', methods=['GET', 'OPTIONS'])
def get_movies():
    if request.method == 'OPTIONS':
        # Respond to the OPTIONS preflight request
        response = app.response_class()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response
    else:
        # Get movies and respond with JSON data
        movies_data = fetch_movies()
        return jsonify(movies_data)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the videotheque page
@app.route('/videotheque')
def videotheque():
    # Load movies data from a file or database
    with open('data.json', 'r') as json_file:
        movies_data = json.load(json_file)
    return render_template('videotheque.html', movies=movies_data)

# Route for the collection page
@app.route('/collection')
def collection():
    # Load user's collection data from a file or database
    return render_template('collection.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
