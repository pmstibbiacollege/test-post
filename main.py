from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route to post a link and receive the result from the link checker app
@app.route('/submit_link', methods=['POST'])
def submit_link():
    link = request.json.get('url')
    if not link:
        return jsonify({"error": "No URL provided"}), 400

    # Send the link to the main app's /check_link endpoint
    try:
        response = requests.post('https://test.sarasequiprnents.com/check_link', data={'url': link})
        # Pass the result from the link checker app back to the client
        return jsonify({"result": response.text})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to connect to link checker app: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5001)
