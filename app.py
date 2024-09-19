from dotenv import load_dotenv
import logging
from flask import Flask, jsonify
from services.iss_service import *
from config.config import Config

load_dotenv()  # This will load the variables from the .env file into the environment
app = Flask(__name__)
app.config.from_object(Config)

logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - &(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logging.info("Starting Flask ISS Tracking App")


@app.route('/api/iss-location', methods=['GET'])
def iss_location():
    logging.info("Received request for ISS location")
    location = get_iss_location()
    return jsonify(location)


@app.route('/api/iss-pass/<float:lat>/<float:lon>', methods=['GET'])
def iss_pass(lat, lon):
    logging.info(f"Received request for ISS pass times for lat: {lat}, lon: {lon}")
    pass_times = get_iss_pass_times(lat, lon)
    return jsonify(pass_times)


@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unhandled exception: {e}")
    return jsonify({'error': 'An internal server error happened'}), 500


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'],
            host=app.config['HOST'], port=app.config['PORT'])
