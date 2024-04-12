import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

def send_request():
    url = "https://shazam.p.rapidapi.com/shazam-events/list"
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),  
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

try:
    data = send_request()
    print(json.dumps(data, indent=4))
except requests.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')