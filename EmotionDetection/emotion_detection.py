import requests, json

def emotion_detector(text_to_analyze):
    response_object = {}
    response_object["anger"] = None
    response_object["disgust"] = None
    response_object["fear"] = None
    response_object["joy"] = None
    response_object["sadness"] = None
    response_object["dominant_emotion"] = None

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 400:
        return response_object

    formatted_response = json.loads(response.text)
    emotion_info = formatted_response['emotionPredictions'][0]['emotion'] 
    response_object["anger"] = emotion_info['anger']
    response_object["disgust"] = emotion_info['disgust']
    response_object["fear"] = emotion_info['fear']
    response_object["joy"] = emotion_info['joy']
    response_object["sadness"] = emotion_info['sadness']
    response_object["dominant_emotion"] = get_dominant_emotion(emotion_info)

    return response_object

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