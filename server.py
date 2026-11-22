"""This is a final project to demonstrate the emotion detector"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """Analyze the input from user"""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!.</b>"

    return (
        f"For the given statment, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f" The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    """Render the template"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
