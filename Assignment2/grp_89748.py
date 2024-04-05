import requests

# Construct the URL for the API endpoint
url = 'https://zenquotes.io/api/random'

try:
    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the JSON response to a Python dictionary
        data = response.json()

        # Extract the quote and author from the response
        quote = data[0]['q']
        author = data[0]['a']

        # Print the quote and author
        print(quote + " - " + author)
    else:
        # If the request was not successful, print an error message
        print("Error:", response.status_code)
except Exception as e:
    # Catch any exceptions that occur during the request
    print("Error:", e)
