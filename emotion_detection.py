import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_info = formatted_response['emotionPredictions'][0]['emotion'] 
    anger_score = emotion_info['anger']
    disgust_score = emotion_info['disgust']
    fear_score = emotion_info['fear']
    joy_score = emotion_info['joy']
    sadness_score = emotion_info['sadness']
    dominant_emotion_name = get_dominant_emotion(emotion_info)

    return { "anger": anger_score,
             "disgust": disgust_score,
             "fear": fear_score,
             "joy": joy_score,
             "sadness": sadness_score,
             "dominant_emotion": dominant_emotion_name }

def get_dominant_emotion(emotions):
    dominant_score = -1
    dominant_emotion = None
    for emotion, score in emotions.items():
        if score > dominant_score:
            dominant_score = score
            dominant_emotion = emotion
    return dominant_emotion

'''
{
  "emotionPredictions": [
    {
      "emotion": {
        "anger": 0.0046455907,
        "disgust": 0.00074047165,
        "fear": 0.007262209,
        "joy": 0.9909928,
        "sadness": 0.019907597
      },
      "target": "",
      "emotionMentions": [
        {
          "span": {
            "begin": 0,
            "end": 18,
            "text": "I'm very happy now"
          },
          "emotion": {
            "anger": 0.0046455907,
            "disgust": 0.00074047165,
            "fear": 0.007262209,
            "joy": 0.9909928,
            "sadness": 0.019907597
          }
        }
      ]
    }
  ],
  "producerId": {
    "name": "Ensemble Aggregated Emotion Workflow",
    "version": "0.0.1"
  }
}
'''