import requests

# Make a GET request to an API endpoint
response = requests.get("http://api.open-notify.org/astros.json")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
    
else:
    # Print the error message
    print('Error:', response.status_code)