import os


class Config:
    DEBUG = os.environ.get('FLASK_DEBUG', True)  # Default to True if not set
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    PORT = int(os.environ.get('FLASK_PORT', 5000))  # Convert PORT to an integer
    ISS_API_BASE_URL = os.environ.get('ISS_API_BASE_URL', 'http://api.open-notify.org')
