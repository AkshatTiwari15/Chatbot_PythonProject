from flask import Flask, render_template, request, jsonify
import random
import re

app = Flask(__name__)
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    if any(greet in user_input for greet in greetings):
        return "Hello! How can I help you today?"

    if "your name" in user_input:
        return "I'm your friendly chatbot. You can call me ChatBuddy."

    if "help" in user_input:
        return "Sure, I'm here to help! Ask me anything."

    if "weather" in user_input:
        return "I can't fetch real-time weather, but it's always sunny in here!"

    if "joke" in user_input:
        jokes = [
            "Why did the computer get cold? Because it forgot to close its Windows!",
            "Why don't robots have brothers? Because they all share the same motherboard!",
            "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'"
        ]
        return random.choice(jokes)

    if re.search(r"\bbye\b|\bexit\b|\bquit\b", user_input):
        return "Goodbye! Have a great day."

    default_responses = [
        "That's interesting! Tell me more.",
        "I'm not sure I understand. Can you elaborate?",
        "Why do you say that?",
        "How does that make you feel?",
        "I see. Go on...",
        "Can you explain that further?",
        "What do you think about that?",
        "Interesting perspective. Let's dive deeper."
    ]
    return random.choice(default_responses)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    bot_response = get_bot_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
