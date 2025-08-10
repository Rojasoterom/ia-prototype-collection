"""Flask server for emotion detection app."""

from flask import Flask, request, jsonify, render_template
from EmotionAnalysis.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    """
    Receives text input, runs emotion analysis, and returns JSON.
    If dominant_emotion is None, returns an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!", 400

    return jsonify(response)

@app.route("/")
def render_index_page():
    """Renders the main HTML interface."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
