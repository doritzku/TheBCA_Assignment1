import os
from dotenv import load_dotenv
import requests

load_dotenv()

url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"

querystring = {"lat":"30.4459","lon":"77.9682","timezone":"auto","language":"en","units":"auto"}

headers = {
	"X-RapidAPI-Key": os.getenv("APIKEY"),
	"X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code != 200:
    print("Error in respose")
    exit(0)

data = response.json()

summary = data['current']['summary']
temp = data['current']['temperature']
humid = data['current']['humidity']

print(f'''
Today will be: {summary } 
and the temperature is: {temp}°C
humidity is: {humid}
''')