import requests
import json
def emotion_detector(text_to_analyze):
    # Define the URL, headers, and input JSON format
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotion_predictions = response_dict.get('emotionPredictions', [])
        emotion_scores = {}
        if emotion_predictions:
            emotions = emotion_predictions[0].get('emotion', {})
            emotion_scores = {key: emotions.get(key, 0) for key in emotions}
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion

        return emotion_scores
    else:
        print(f"Error: {response.status_code}")
        return None




