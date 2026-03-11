import asyncio
import threading
import time

from backend.exchanges.binance import BinanceClient
from backend.exchanges.bybit import BybitClient
from backend.config import BINANCE_KEY, BINANCE_SECRET, BYBIT_KEY, BYBIT_SECRET
from backend.api.server import stats
from backend.market.cache import get_prices_snapshot
from backend.market.binance_ws import run_binance_ws
from backend.market.bybit_ws import run_bybit_ws


def build_demo_prices(snapshot: dict):
    prices = {}

    # берём сначала Binance, если есть, иначе Bybit
    for symbol in ["BTC/USDT", "ETH/BTC", "ETH/USDT"]:
        b_key = f"binance:{symbol}"
        y_key = f"bybit:{symbol}"

        if b_key in snapshot:
            prices[symbol] = snapshot[b_key]["bid"]
        elif y_key in snapshot:
            prices[symbol] = snapshot[y_key]["bid"]

    return prices


def arbitrage_loop():
    print("Starting arbitrage engine...")

    try:
        binance = BinanceClient(BINANCE_KEY, BINANCE_SECRET)
        bybit = BybitClient(BYBIT_KEY, BYBIT_SECRET)

        binance_markets = binance.load_markets()
        bybit_markets = bybit.load_markets()

        print("Binance markets:", len(binance_markets))
        print("Bybit markets:", len(bybit_markets))

    except Exception as e:
        print("Exchange startup error:", str(e))

    while True:
        try:
            snapshot = get_prices_snapshot()
            stats["prices_count"] = len(snapshot)

            prices = build_demo_prices(snapshot)

            if all(k in prices for k in ["BTC/USDT", "ETH/BTC", "ETH/USDT"]):
                value = prices["ETH/USDT"] / (prices["BTC/USDT"] * prices["ETH/BTC"])

                if value > 1.003:
                    stats["profit"] += round(value - 1, 6)
                    stats["trades"] += 1
                    stats["last_opportunity"] = {
                        "route": "USDT -> BTC -> ETH -> USDT",
                        "value": round(value, 6)
                    }

            time.sleep(3)

        except Exception as e:
            print("Arbitrage loop error:", str(e))
            time.sleep(5)


async def ws_main():
    await asyncio.gather(
        run_binance_ws(),
        run_bybit_ws(),
    )


def start_background_loop():
    thread = threading.Thread(target=arbitrage_loop, daemon=True)
    thread.start()


if __name__ == "__main__":
    start_background_loop()
    asyncio.run(ws_main())