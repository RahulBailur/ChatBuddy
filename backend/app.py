from flask import Flask, request, jsonify
from model import get_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chat requests and returns AI-generated responses."""
    data = request.get_json()
    user_input = data.get("query", "").strip()

    if not user_input:
        return jsonify({"error": "Empty input"}), 400

    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
