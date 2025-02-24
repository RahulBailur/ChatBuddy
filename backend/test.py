from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    return jsonify({"response": f"Hello, you said: {data['query']}"})

if __name__ == "__main__":
    app.run(debug=True)
