import os

BINANCE_KEY = os.getenv("BINANCE_KEY", "")
BINANCE_SECRET = os.getenv("BINANCE_SECRET", "")

BYBIT_KEY = os.getenv("BYBIT_KEY", "")
BYBIT_SECRET = os.getenv("BYBIT_SECRET", "")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT = os.getenv("TELEGRAM_CHAT", "")

TRADE_SIZE = float(os.getenv("TRADE_SIZE", "50"))
MIN_PROFIT = float(os.getenv("MIN_PROFIT", "0.003"))
