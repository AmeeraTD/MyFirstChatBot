from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")

    # Simple rule-based replies
    if "hello" in user_input.lower():
        response = "Hey there! 👋"
    elif "how are you" in user_input.lower():
        response = "I'm a bot, but I'm doing well! Thanks for asking 😊"
    elif "bye" in user_input.lower():
        response = "See you later! 👋"
    else:
        response = "Hmm... I’m not sure how to respond to that 🤔"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
