from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "sentiment analysis is running"

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity

    if sentiment_score > 0:
        sentiment = "Positive"

    elif sentiment_score < 0:
        sentiment = "Negative"
    
    else:
        sentiment = "Neutral"

    return jsonify({"sentiment": sentiment, "score": sentiment_score})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
