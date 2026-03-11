import time
import threading

from backend.exchanges.binance import BinanceClient
from backend.exchanges.bybit import BybitClient
from backend.engine.arbitrage import find_arbitrage
from backend.config import (
    BINANCE_KEY,
    BINANCE_SECRET,
    BYBIT_KEY,
    BYBIT_SECRET,
)

from backend.api.server import stats


def arbitrage_loop():

    print("Starting arbitrage engine...")

    binance = BinanceClient(BINANCE_KEY, BINANCE_SECRET)
    bybit = BybitClient(BYBIT_KEY, BYBIT_SECRET)

    try:

        binance_markets = binance.load_markets()
        bybit_markets = bybit.load_markets()

        print("Binance markets:", len(binance_markets))
        print("Bybit markets:", len(bybit_markets))

        # тестовые символы (позже будем брать автоматически)
        symbols = [
            "BTC/USDT",
            "ETH/BTC",
            "ETH/USDT"
        ]

        while True:

            try:

                # тестовые цены (потом заменим на реальные)
                prices = {
                    "BTC/USDT": 60000,
                    "ETH/BTC": 0.05,
                    "ETH/USDT": 3100
                }

                opportunities = find_arbitrage(symbols, prices)

                if opportunities:

                    best = opportunities[0]

                    print("Arbitrage found:", best)

                    stats["profit"] += best["profit"]
                    stats["trades"] += 1

                time.sleep(3)

            except Exception as e:
                print("Engine error:", str(e))
                time.sleep(5)

    except Exception as e:

        print("Startup error:", str(e))


def start():

    thread = threading.Thread(target=arbitrage_loop)

    thread.daemon = True

    thread.start()


if __name__ == "__main__":

    start()

    while True:
        time.sleep(60)
