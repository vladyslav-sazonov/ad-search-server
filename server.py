import json
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
CORS(app)


@app.route('/find_adverts', methods=['POST'])
def get_letter_predict():
    texts = request.get_json()
    prediction = [
                    {'text': 'With DermaSun cream you will feel like your skin is perfectly soft.', 'confidence': 0.88},
                    {'text': 'No matter if you-re in the mountains or at the beach, your Flachsmann is always there with you.', 'confidence': 0.45},
                    {'text': 'We LOVE this travel clutch.', 'confidence': 0.88},
                    {'text': 'If your body does a sport, your wrist needs this Garmin vivoactive watch.', 'confidence': 0.91},
                    {'text': 'WCapture every situation exquisitely with manual controls on the #GalaxyS6edgePlus 16MP camera.', 'confidence': 0.73},
                ]
    return jsonify(prediction)

@app.after_request
def after_request(response):
    """ Logging after every request. """
    # This avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.

    #if response.status_code != 500:
        #app.logger.info(
        #    json.dumps(json.loads(response.response.decode("utf-8")), indent=4)
        #)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)
