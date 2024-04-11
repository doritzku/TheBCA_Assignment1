import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "f2ac725867msh024f9ec302e02edp10edf1jsn6accedd0b37e",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

# Function to format the output with color and styling
def format_output(language, code):
    return f"\033[1mLanguage:\033[0m {language} \033[1m|\033[0m \033[1mLanguage Code:\033[0m {code}"

# Printing the formatted output
print("\033[1m" + "Language List:" + "\033[0m")
for language, code in data["data"]["languages"].items():
    print(format_output(language, code))
