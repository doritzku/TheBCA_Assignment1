import requests

response = requests.get('https://zenquotes.io/api/random')

if response.status_code == 200:
    print(response.text)
else:
    print('Error:', response.status_code)