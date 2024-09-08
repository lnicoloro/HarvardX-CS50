import json
import requests
import sys

while True:
    try:
        if len(sys.argv) == 2:
            n = float(sys.argv[1])
            break
        else:
            sys.exit('Missing command-line argument')
    except ValueError:
        sys.exit('Command-line argument is not a number')



response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
coin = response.json()['bpi']['USD']['rate_float']

amount = coin * n
print(f"${amount:,.4f}")