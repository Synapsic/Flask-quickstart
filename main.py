from flask import Flask, request, jsonify, send_from_directory
import requests
import os

SYNAPSE_API = "https://synapse-api.replit.app/api"

# replace this by your Synapse Application credentials
CLIENT_ID = "test_app"
CLIENT_SECRET = os.getenv("SYNAPSE_SECRET")

app = Flask(__name__)

# main route for Synapse authorization
@app.route("/synapse/token", methods=["GET"])
def synapse_token():
    
    url = f"{SYNAPSE_API}/token?code={request.args.get('code')}"
    response = requests.get(url, headers={
        "Authorization": f"Basic {CLIENT_ID}:{CLIENT_SECRET}"
    })

    # a JSON object is returned with token or error
    return jsonify(response.json())

# static files (html, css, ...) served from /public
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_static_files(path):
    
    path = path if path != "" and path is not None else "index.html"
    static_dir = os.path.join(os.getcwd(), "public")

    return send_from_directory(static_dir, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)