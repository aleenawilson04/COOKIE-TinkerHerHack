from flask import Flask, render_template, request, jsonify
import requests
import os
import google.generativeai as genai


app = Flask(__name__)
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
@app.route('/events', methods=['GET'])
def get_events():
    location = request.args.get('location', 'New York')
    
    try:
        # Query Gemini to generate event recommendations
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"List upcoming tech events in {location} with details.")

        return jsonify({"events": response.text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
# Get API key from environment variables
API_KEY = os.environ.get('EVENTS_API_KEY')
API_URL = 'https://www.eventbriteapi.com/v3/events/search/'  # Ensure this is correct

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events', methods=['GET'])
def get_events():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location is required'}), 400

    # Ensure API key is available
    if not API_KEY:
        return jsonify({'error': 'Missing API key'}), 401

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }
    params = {
        "location.address": location,  
        "expand": "venue"
    }

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        
        # Debugging log
        print(f"API URL: {response.url}")  
        print(f"Status Code: {response.status_code}")  
        print(f"Response Text: {response.text}")  

        response.raise_for_status()
        data = response.json()

        events = [
            {
                "title": event.get("name", {}).get("text", "No Title"),
                "description": event.get("description", {}).get("text", "No Description"),
                "date": event.get("start", {}).get("local", "No Date"),
                "image": event.get("logo", {}).get("url", ""),
                "venue": event.get("venue", {}).get("address", {}).get("localized_address_display", "No Venue")
            }
            for event in data.get("events", [])
        ]

        return jsonify(events)

    except requests.exceptions.HTTPError as e:
        return jsonify({'error': f'HTTP Error: {e}, Response: {response.text}'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request failed: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
