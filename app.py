import os
from flask import Flask, render_template, request, jsonify

try:
    from openai import OpenAI
except ImportError:
    raise SystemExit("The 'openai' package is required. Install it with 'pip install openai'.")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return jsonify({"error": "OPENAI_API_KEY is not set"}), 500
    data = request.get_json() or {}
    user_message = data.get("message", "")
    client = OpenAI(api_key=api_key)
    response = client.responses.create(model="gpt-4o-mini", input=user_message)
    reply = response.output[0].content[0].text
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
