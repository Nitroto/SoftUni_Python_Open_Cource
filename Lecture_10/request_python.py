import requests
from decimal import Decimal

value_for_exchange = input('Enter a sum: ')
currency_key = input('Enter a currency: ')
resp = requests.get('http://api.fixer.io/latest?base=BGN')
data = resp.json()['rates']
currency_rate = data[currency_key]
exchanged_value = Decimal(value_for_exchange) / currency_rate
print(exchanged_value)
