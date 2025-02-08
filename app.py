from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Replace with your actual API key and endpoint
API_KEY = os.getenv('VN6Q7C3ODPVNK74GUN')  # Store your API key in an environment variable
API_URL = 'https://api.example.com/events'  # Replace with the actual API URL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events', methods=['GET'])
def get_events():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location is required'}), 400

    # Make a request to the external API
    try:
        response = requests.get(API_URL, params={'location': location, 'key': API_KEY})
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

    events = response.json()
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)