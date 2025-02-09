from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get('EVENTS_API_KEY')  # Store API key in environment variable
API_URL = 'https://www.eventbriteapi.com/v3/events/search/'  # Correct API endpoint

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events', methods=['GET'])
def get_events():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location is required'}), 400

    # Make a request to the Eventbrite API
    try:
        response = requests.get(
            f'{API_URL}events/search/',
            params={
                'q': location,  # Search query (location or event name)
                'token': API_KEY,  # Your Eventbrite API token
                'expand': 'venue'  # Optional: Include venue details
            }
        )
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

    # Parse the response and extract events
    events = response.json().get('events', [])
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
