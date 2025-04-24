"""Flask web server for emotion detection using IBM Watson NLP"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """Handles GET request and returns formatted emotion detection results."""
    # Get user input from query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Run the emotion detector
    result = emotion_detector(text_to_analyze)

    # Check for invalid input (i.e., no dominant emotion detected)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Build the formatted string output
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def index():
    """Renders the web interface for the application."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)
