'''
Emotion detector module
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    Function to return the result of the analysis
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "<p>Invalid text! Please try again!</p>"

    web_response = f"""<p>For the given statement, the system response is
                    'anger': { response["anger"] }, 
                    'disgust': { response["disgust"] }, 
                    'fear': { response["fear"] }, 
                    'joy': { response["joy"] } and 
                    'sadness': { response["sadness"] }. 
                    The dominant emotion is <b>{ response["dominant_emotion"] }</b>.</p>"""

    return web_response

@app.route("/")
def render_index_page():
    '''
    Function to render index
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8080)
