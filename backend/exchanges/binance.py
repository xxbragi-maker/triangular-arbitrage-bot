import ccxt

class BinanceClient:

    def __init__(self, api_key, secret):

        self.exchange = ccxt.binance({
            "apiKey": api_key,
            "secret": secret,
            "enableRateLimit": True
        })

    def load_markets(self):
        return self.exchange.load_markets()
