import requests
from flask import Flask, jsonify
from config.config import Config
from utils.time_utils import convert_timestamp


app = Flask(__name__)
app.config.from_object(Config)


def get_iss_location():
    response = requests.get(f"{Config.ISS_API_BASE_URL}/iss-now.json")
    if response.status_code == 200:
        data = response.json()
        timestamp = convert_timestamp(data['timestamp'])
        return {
            'timestamp': timestamp,
            'latitude': data['iss_position']['latitude'],
            'longitude': data['iss_position']['longitude']
        }
    else:
        return {'error': 'Unable to fetch ISS location'}


def get_iss_pass_times(lat, lon):
    """
    DEPRECATED: ISS Pass predictions are now turned off.
    Real time current ISS location and number of people in space will continue to operate.
    """
    params = {
        'lat': lat,
        'lon': lon
    }
    response = requests.get(
        f"{Config.ISS_API_BASE_URL}/iss-pass.json", params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'latitude': data['request']['latitude'],
            'longitude': data['request']['longitude'],
            'passes': data['response']
        }
    else:
        return {'error': 'Unable to fetch ISS pass times'}


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
