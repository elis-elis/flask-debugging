# API calls and data processing are handled in iss_service.py

import requests
import logging
from config.config import Config
from utils.time_utils import convert_timestamp


# configure logging
logging.basicConfig(
    level=Config.LOG_LEVEL,
    format='%(asctime)s - &(levelname)s - %(message)s'
)


def get_iss_location():
    try:
        response = requests.get(f"{Config.ISS_API_BASE_URL}/iss-now.json")
        if response.status_code == 200:
            data = response.json()
            timestamp = convert_timestamp(data['timestamp'])
            logging.info(f"Fetched ISS location: {data['iss_position']}")
            return {
                'timestamp': timestamp,
                'latitude': data['iss_position']['latitude'],
                'longitude': data['iss_position']['longitude']
            }
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error while fetching ISS location: {http_err}")
        return {'error': 'HTTP error occurred while fetching ISS location'}, 500
    except Exception as err:
        logging.error(f"Unexpected error: {err}")
        return {'error': 'Unexpected error occurred while fetching ISS location'}, 500


def get_iss_pass_times(lat, lon):
    """
    DEPRECATED: ISS Pass predictions are now turned off.
    Real time current ISS location and number of people in space will continue to operate.
    """
    try:
        params = {
            'lat': lat,
            'lon': lon
        }
        response = requests.get(
            f"{Config.ISS_API_BASE_URL}/iss-pass.json", params=params)
        if response.status_code == 200:
            data = response.json()
            logging.info(f"Fetched ISS pass times for lat: {lat}, lon: {lon}")
            return {
                'latitude': data['request']['latitude'],
                'longitude': data['request']['longitude'],
                'passes': data['response']
            }
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error while fetching ISS pass times: {http_err}")
        return {'error': 'HTTP error occurred while fetching ISS pass times'}, 500
    except Exception as err:
        logging.error(f"Unexpected error: {err}")
        return {'error': 'Unexpected error occurred while fetching ISS pass times'}, 500
