import sqlite3
import alpaca_trade_api as tradeapi
from decouple import config


connection = sqlite3.connect("app.db")
cursor = connection.cursor()
api = tradeapi.REST(config('API_KEY'), config('SECRET'), base_url='https://paper-api.alpaca.markets') #using env variables for sake of privacy

assets = api.list_assets()

for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable:
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)
connection.commit()