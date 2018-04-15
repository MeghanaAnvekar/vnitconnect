import json
from flask import  request
from flask import Flask
from _firebase import fetch_data



# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
	answer = "la la land "
	req = request.get_json(silent=True, force=True)
 	#question = req.get('result').get('resolvedQuery') 
 	#answer = fetch_data(question)
    	print("Request:")
    	print(json.dumps(req, indent=4))

	xyz = str(json.dumps(req, indent=4))
	res = {
	"speech": "webhook working",
	"displayText": xyz,
	"source": "webhookdata"
	}
	r = json.dumps(res)
	return r

if __name__ == '__main__' :
    app.run(debug='true')
