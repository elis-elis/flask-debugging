from datetime import datetime


def convert_timestamp(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
