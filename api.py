import requests
import csv
from pprint import pprint

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")

data = response.json()

rates = data[0]["rates"]

headers_of_columns = list(rates[0].keys())

pprint(rates)


codes_of_currencies = []
for x in range(len(rates)):
    code_of_currency = rates[x]['code']
    codes_of_currencies.append(code_of_currency)
print(codes_of_currencies)

writer = csv.DictWriter (open('rates.csv', 'w', newline=''),delimiter=';', fieldnames=headers_of_columns)
writer.writeheader()
writer.writerows(rates)
