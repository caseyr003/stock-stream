import requests
import json

class StockAPI():
    def __init__(self):
        self.url = "https://api.iextrading.com/1.0"

    def get_history(self, stock_symbol, period):
        endpoint='%s/stock/%s/chart/%s' % (self.url, stock_symbol, period)
        return json.loads(requests.request("GET", endpoint).text)

    def get_info(self, stock_symbol):
        endpoint='%s/stock/%s/company' % (self.url, stock_symbol)
        return json.loads(requests.request("GET", endpoint).text)

    def get_name(self, stock_symbol):
        endpoint='%s/stock/%s/company' % (self.url, stock_symbol)
        return json.loads(requests.request("GET", endpoint).text)['companyName']

    def get_price(self, stock_symbol):
        endpoint='%s/stock/%s/quote' % (self.url, stock_symbol)
        return json.loads(requests.request("GET", endpoint).text)['latestPrice']

    def get_stock_data(self, stock_symbol):
        endpoint='%s/stock/%s/quote' % (self.url, stock_symbol)
        data = json.loads(requests.request("GET", endpoint).text)
        return data['latestPrice'], data['companyName']
