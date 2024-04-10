import requests
from colorama import Fore, Style

# Install colorama if you haven't already
# pip install colorama

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

querystring = {
    "symbol": "AAPL",
    "interval": "5m",
    "range": "1d",
    "region": "US",
    "comparisons": "^GDAXI,^FCHI"
}

headers = {
    "X-RapidAPI-Key": "59f7f9c614msh0ad385a9e3b7f05p1cf79bjsn66134cc6dfe6",
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    # Print data with different colors
    print(Fore.GREEN + "Timestamp".ljust(20), "Open".ljust(10), "High".ljust(10), "Low".ljust(10), "Close".ljust(10), "Volume".ljust(10), "Adj Close".ljust(10))
    print(Style.RESET_ALL)  # Reset color

    timestamps = data['chart']['result'][0]['timestamp']
    opens = data['chart']['result'][0]['indicators']['quote'][0]['open']
    highs = data['chart']['result'][0]['indicators']['quote'][0]['high']
    lows = data['chart']['result'][0]['indicators']['quote'][0]['low']
    closes = data['chart']['result'][0]['indicators']['quote'][0]['close']
    volumes = data['chart']['result'][0]['indicators']['quote'][0]['volume']
    
    for i in range(len(timestamps)):
        timestamp = timestamps[i]
        open_price = opens[i]
        high_price = highs[i]
        low_price = lows[i]
        close_price = closes[i]
        volume = volumes[i]
        
        # 'adjclose' is not always present, handle it gracefully
        adj_close = data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose'][i] if 'adjclose' in data['chart']['result'][0]['indicators'] else None

        print(Fore.BLUE + str(timestamp).ljust(20), str(open_price).ljust(10), str(high_price).ljust(10), str(low_price).ljust(10), str(close_price).ljust(10), str(volume).ljust(10), str(adj_close).ljust(10))
        print(Style.RESET_ALL)  # Reset color
else:
    print(Fore.RED + "Failed to fetch data. Status code:", response.status_code)
    print(Style.RESET_ALL)  # Reset color

