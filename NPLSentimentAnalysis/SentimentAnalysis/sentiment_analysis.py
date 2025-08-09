'''
This file include the function to make sentiment analyzis by
using BERT sentiment analyzer by Watson
'''
import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    response = requests.post(url, json=myobj, headers=header)

    try:
        formatted_response = response.json()  # ✅ más seguro que json.loads(response.text)

        if 'documentSentiment' not in formatted_response:
            print("Error: The response don't have 'documentSentiment'")
            print("Content recieved:", formatted_response)
            return {"Error": "Unespected API response"}

        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        return {'label': label, 'score': score}

    except json.JSONDecodeError:
        print("Error decoding JSON. raw response:")
        print(response.text)
        return {"Error": "non valid JSON response."}

    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"Error": str(e)}