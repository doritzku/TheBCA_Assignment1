import requests;


KEY_COLOR = "\033[94m"  # Blue
VALUE_COLOR = "\033[92m"  # Green
RESET_COLOR = "\033[0m"  # Reset color

url = "https://imdb188.p.rapidapi.com/api/v1/searchIMDB"

querystring = {"query":"movie"}

headers = {
	"X-RapidAPI-Key": "2b5f974b6cmsha001208ca38d067p1f2e72jsn0f34c37a9899",
	"X-RapidAPI-Host": "imdb188.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data=response.json()
for key, value in data.items():
        if isinstance(value, list):
            print(KEY_COLOR + key + ":" + RESET_COLOR)
            for item in value:
                for subkey, subvalue in item.items():
                    if subkey not in ["qid", "q"]:  # Exclude qid and q keys
                        print(KEY_COLOR + subkey + ":" + RESET_COLOR, VALUE_COLOR + str(subvalue) + RESET_COLOR)
                print()
        else:
            print(KEY_COLOR + key + ":" + RESET_COLOR, VALUE_COLOR + str(value) + RESET_COLOR)


#Additional, if you want the data to be displayed in a different form.
#data = json.loads(response.text)
#formattedData = json.dumps(data, indent=4)
#print(formattedData)



