"""
This module defines a Flask application for emotion detection.
"""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint for emotion detection.

    Retrieves the 'textToAnalyze' parameter from the request and
    uses the emotion_detector function to analyze the text.
    Returns the emotion scores or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response and response['dominant_emotion'] is not None:
        label = response['dominant_emotion']
        score1 = response['anger']
        score2 = response['disgust']
        score3 = response['fear']
        score4 = response['joy']
        score5 = response['sadness']
        return (
    f"The given statement triggers 'anger': {score1}, "
    f"'disgust': {score2}, 'fear': {score3}, 'joy': {score4}, "
    f"and 'sadness': {score5}. The dominant emotion is {label}.")

    return "Invalid text! Please try again."

@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
