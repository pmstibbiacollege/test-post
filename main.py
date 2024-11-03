from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Route to post a link and receive the result from the link checker app
@app.route('/submit_link', methods=['POST'])
def submit_link():
    # Read the URL from link.txt
    try:
        with open('link.txt', 'r') as file:
            link = file.read().strip()
    except FileNotFoundError:
        return jsonify({"error": "link.txt file not found"}), 500
    except Exception as e:
        return jsonify({"error": f"Error reading link.txt: {str(e)}"}), 500

    if not link:
        return jsonify({"error": "No URL found in link.txt"}), 400

    # Send the link to the main app's /check_link endpoint
    try:
        response = requests.post('https://test.sarasequiprnents.com/check_link', data={'url': link})
        # Pass the result from the link checker app back to the client
        return jsonify({"result": response.text})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to connect to link checker app: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5001)
