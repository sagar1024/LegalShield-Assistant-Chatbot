import requests

def fetch_data(url: str, params: dict = {}):
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None
