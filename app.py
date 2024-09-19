from dotenv import load_dotenv
from flask import Flask, jsonify
from services.iss_service import *
from config.config import Config


load_dotenv()   # This will load the variables from the .env file into the environment
app = Flask(__name__)
app.config.from_object(Config)


@app.route('/api/iss-location', methods=['GET'])
def iss_location():
    location = get_iss_location()
    return jsonify(location)


@app.route('/api/iss-pass/<float:lat>/<float:lon>', methods=['GET'])
def iss_pass(lat, lon):
    pass_times = get_iss_pass_times(lat, lon)
    return jsonify(pass_times)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'],
            host=app.config['HOST'], port=app.config['PORT'])
