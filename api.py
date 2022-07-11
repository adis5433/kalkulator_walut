import requests
import csv
from pprint import pprint

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")

data = response.json()

rates = data[0]["rates"]

headers_of_columns = list(rates[0].keys())

print(rates)

print(headers_of_columns)
codes_of_currencies = []
for x in range(len(rates)):
    code_of_currency = rates[x]['code']
    codes_of_currencies.append(code_of_currency)
print(codes_of_currencies)


with open('rates.csv', 'w', newline='') as csvfile:
    fieldnames = headers_of_columns
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

    writer.writeheader()
    for data in rates:
        writer.writerow(data)

