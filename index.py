from flask import Flask, request, jsonify, render_template
import os
import requests
import dialogflow
import requests
import json
import pusher
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/webhook', methods=['POST'])
def webhook():
    
    data = request.get_json(silent=True)
    #k=data['queryResult']['parameters']["tournament"]
    #sen=data['queryResult']['queryText']
    resp= {"fulfillmentMessages":[{"card":{"title":"kj","subtitle":"jn","imageUri":"https://www.fcbarcelonanoticias.com/uploads/s1/22/08/83/meme-cr7-220883.jpeg"},"platform":"FACEBOOK"},{"text":{"text":["hello"]}}]} 
    return jsonify(resp)

def teamMenber(k):
    import urllib.request as r
    sol=json.loads(requests.get("https://apiv2.apifootball.com/?action=get_players&player_name="+k+"&APIkey=ab601b8d06cadb81db396e987358e0d8cbc06141c2f27c6cfca81cafa358c6ea").text)
    return ' '.join(sol.values())
def countries():
    import urllib.request as r
    sol=json.loads(requests.get("https://apiv2.apifootball.com/?action=get_countries&APIkey=ab601b8d06cadb81db396e987358e0d8cbc06141c2f27c6cfca81cafa358c6ea").text)
    return ' '.join(sol.values())
def odds():
    import urllib.request as r
    sol=json.loads(requests.get("https://apiv2.apifootball.com/?action=get_odds&from="+x1+"&to="+x2+"&APIkey=ab601b8d06cadb81db396e987358e0d8cbc06141c2f27c6cfca81cafa358c6ea").text)
    return ' '.join(sol.values())
def meme(query):
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img".format(q=query))
    images = driver.find_elements_by_tag_name('img')
    images=[x.get_attribute('src') for x in images]
    return images

def score(k,sen):
    import urllib.request as r
    sol=json.loads(requests.get("https://apiv2.apifootball.com/?action=get_leagues&APIkey=ab601b8d06cadb81db396e987358e0d8cbc06141c2f27c6cfca81cafa358c6ea").text)
    sol=[x for x in sol if(x["league_name"].lower()==k.lower())]
    sentiment=sen
    dic=dict()
    dic["text"]=sentiment
    sentiment=json.loads(requests.post("http://text-processing.com/api/sentiment/",dic).text)
    #(' '.join(sol[0].values())+
    return sentiment['label']
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response.query_result.fulfillment_text
@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = { "message":  fulfillment_text }
    return jsonify(response_text)
# run Flask app
def create_poll():
    pass

if __name__ == "__main__":
    
    app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']
  
    app.run()
