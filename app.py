import json
from flask import  request
from flask import Flask
from _firebase import fetch_data



# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
	
	res = {
	"speech": "webhook working",
	"displayText": "webhook ",
	"source": "webhookdata"
	}
	r = json.dumps(res)
	return r

if __name__ == '__main__' :
    app.run(debug='true')
