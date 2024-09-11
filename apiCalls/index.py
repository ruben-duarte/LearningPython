import requests
import json
from dataclasses import dataclass, asdict
from typing import Optional
import datetime
import time

API_KEY = "J2FV7aKrcCaZtMlHb3pU74GHQKVLUZip3rXTv0Mb"
BASE_URL = "https://yfapi.net/v6/finance"
QUOTE_URL = BASE_URL + "/quote"
OPTIONS_URL = BASE_URL + "/options"
SPARK_URL = BASE_URL + "/spark"

header = {
    'X-API-KEY': API_KEY,
    'User-Agent': 'Mozilla/5.0'
    }

@dataclass
class QuotationParams:
    symbols: str
    lang: Optional[str] = None
    region: Optional[str] = None

def get_quotation(search):
    search_params = asdict(search)
    response = requests.get(QUOTE_URL,params=search_params,headers=header).json()
    print(json.dumps(response, indent=2))

def get_options(symbol):
    d = '22/03/2022'
    timestamp = int(time.mktime(datetime.datetime.strptime(d, '%d/%m/%Y').timetuple()))

    URL=('https://yfapi.net/v7/finance/options/'
        '{}?'
        'date={}'
        )
    URL=URL.format(symbol, timestamp)
    header = {
        'X-API-KEY': 'J2FV7aKrcCaZtMlHb3pU74GHQKVLUZip3rXTv0Mb',
        'User-Agent': ''
        }
        
    response = requests.request('GET', URL, headers=header).json()
    print("---- options")
    print(json.dumps(response, indent=4))

def history_data(symbol):
    interval='1d'
    range='5d'
    symbols=symbol # AAPL is the symbol for Apple Inc.
    URL=('https://yfapi.net/v8/finance/spark?'
        'interval={}&'
        'range={}&'
        'symbols={}'
        )
    URL=URL.format(interval,range,symbols)

    header = {
        'X-API-KEY': 'J2FV7aKrcCaZtMlHb3pU74GHQKVLUZip3rXTv0Mb',
        'User-Agent': ''
        }
    response = requests.request('GET', URL, headers=header).json()
    print(json.dumps(response, indent=4))


def main():
    search_quote = QuotationParams(
        symbols = "TWTR,EURUSD=X,AAPL",
        lang = "en",
        region = "US"
    )
    print("====Quotation==== ")
    get_quotation(search_quote)
    print("====Options==== ")
    get_options("AAPL")
    print("====History data==== ")
    history_data("AAPL")

   
if __name__ == "__main__":
    main()