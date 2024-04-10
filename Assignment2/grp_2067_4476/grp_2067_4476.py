import os
from dotenv import load_dotenv
import requests

load_dotenv()

url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"Python developer in Texas, USA","page":"1","num_pages":"1"}

headers = {
	"X-RapidAPI-Key": os.getenv("APIKEY"),
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code != 200:
    print("Error in respose")
    exit(0)

data = response.json()['data']

for job in data:
    print(f'''
Job at: {job['employer_name']}
Job Description: {job['job_description']}\n
    ''')
