import json
import requests
#from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return ('Error: the translation service is not configured.')
    url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(source_language, dest_language)
    header = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'], 'Content-Type': 'application/json; charset=UTF-8'}
    payload = [{'Text': text}]
    r = requests.post(url, data=str(payload), headers=header)
    if r.status_code != 200:
        return ('Error: the translation service failed.')
    #print(json.loads(r.content.decode('utf-8-sig')))
    #print(json.loads(r.content.decode('utf-8-sig'))[0]['text'])
    return json.loads(r.content.decode('utf-8-sig'))[0]['translations'][0]['text']
