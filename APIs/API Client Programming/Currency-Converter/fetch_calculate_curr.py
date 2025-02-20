import requests
import sys

def get_exchange_rate(target_currency):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        rates = response.json()
        exchange_rate = rates['rates'].get(target_currency.upper(), 'N/A')

        if exchange_rate == 'N/A':
            print(f"Currency {target_currency} not found.")
        else:
            print(f"1 USD = {exchange_rate} {target_currency.upper()}")
    else:
        print("Failed to fetch exchange rates.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <CURRENCY_CODE>")
    else:
        get_exchange_rate(sys.argv[1])
