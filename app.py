from flask import Flask, request, redirect,render_template, url_for
import requests
import csv
from pprint import pprint

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")

data = response.json()



rates = data[0]["rates"]

headers_of_columns = list(rates[0].keys())

pprint(rates)


codes_of_currencies = []
x = 0
for _ in rates:
    code_of_currency = rates[x]['code']
    codes_of_currencies.append(code_of_currency)
    x += 1

def search_bid_value_by_code(code_of_currecy):
    for currency in rates:
        if currency['code'] == code_of_currecy:
            return currency['bid']

def convert_to_pln(code_of_currecy,amount_of_currency):
    cost_of_operation = float(amount_of_currency) * search_bid_value_by_code(code_of_currecy)
    return cost_of_operation


app = Flask(__name__)

@app.route("/kalkulator", methods = ["GET"])
def currencies():
    currencies = codes_of_currencies
    return render_template("kalkulator_walut.html", currencies=currencies)


@app.route("/kalkulator", methods = ["GET","POST"])
def convert_curr():
    if request.method == "POST":
        code_of_currency_to_buy = request.form["currency"]
        amount_currency_user_want_to_buy = request.form["amonunt_of_currency"]
        cost_of_operation = convert_to_pln(code_of_currency_to_buy,amount_currency_user_want_to_buy)
        return render_template("kalkulator_walut_result.html", cost=round(cost_of_operation,2))
    

@app.route("/result")
def show_result(cost):
    return render_template("kalkulator_walut_result.html")
