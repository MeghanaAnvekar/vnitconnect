import json
from flask import Flask


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():



    res = {
        "speech": "webhook working",
        "displayText": "webhook working",
        "source": "webhookdata"
    }
    r = json.dumps(res)
    return r

if __name__ == '__main__' :
    app.run(debug='true')
