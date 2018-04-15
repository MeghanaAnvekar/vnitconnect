import json
from flask import  request
from flask import Flask
from flask import jsonify
from _firebase import fetch_data, fetch_questions



# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook_dialogflow():
	data = request.get_json()
 
    	question = data['result']['resolvedQuery']
 	answer = fetch_data(question)
 	
	res = {
	"speech": answer,
	"displayText":answer,
	"source": "webhookdata"
	}
	
	return jsonify(res)
	
	
@app.route('/questions', methods=['POST'])
def webhook_android_app():
	data = request.get_json()
	question = data['question']
	question_list = fetch_questions(question)
	res = {
	"question_list": question_list
	}
	return jsonify(res) 

if __name__ == '__main__' :
    app.run(debug='true')
