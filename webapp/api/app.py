import os

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from models import Patient

GET_METHOD = 'GET'
POST_METHOD = 'POST'
PUT_METHOD = 'PUT'
ID = 'id'
DB_URL = os.getenv('DB_URL')
print(DB_URL)
app = Flask(__name__)

# Initialize flask app for the example
app.debug = True
app.config['PATH_INFO'] = os.environ.get('APPLICATION_ROOT', '')
app.config['SECRET_KEY'] = 'ffffff'

cors = CORS(app)


@app.route('/', methods=[GET_METHOD])
@cross_origin()
def home():
    return jsonify({})


@app.route('/patients', methods=[GET_METHOD])
@cross_origin()
def api_get_patients():
    return jsonify(Patient.list_all())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
