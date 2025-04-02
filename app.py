from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("🔑 OPENROUTER_API_KEY:", OPENROUTER_API_KEY)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")

    try:
        # Make request to OpenRouter
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct",  # You can try other free models too
                "messages": [
                    {"role": "system", "content": "You are a helpful chatbot."},
                    {"role": "user", "content": user_input}
                ]
            }
        )

        result = response.json()
        reply = result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print("🔥 ERROR:", e)
        print("🔥 FULL RESPONSE:", response.text)
        reply = "Oops! Something went wrong."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
