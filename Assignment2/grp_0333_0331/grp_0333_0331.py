import os
from dotenv import load_dotenv
import requests

load_dotenv()

url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country":"India"}

headers = {
	"X-RapidAPI-Key": os.getenv("APIKEY"),
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()['response'][0]

print(f'''
In India,
cases: {data['cases']['total']}
deaths: {data['deaths']['total']}
tests: {data['tests']['total']}
''')