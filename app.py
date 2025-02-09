from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Load Gemini API Key
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure it's set in your environment

# Configure Google Generative AI
genai.configure(api_key=GENAI_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events', methods=['GET'])
def get_events():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location is required'}), 400

    prompt = f"List some interesting upcoming tech and community events in {location} with date, venue, and a brief description."

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        if response and response.text:
            events = response.text.split("\n")  # Basic parsing (adjust as needed)
            return jsonify({"events": events})
        else:
            return jsonify({'error': 'No events found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
