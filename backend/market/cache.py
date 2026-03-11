import threading

market_prices = {}
_lock = threading.Lock()


def update_price(symbol: str, bid: float, ask: float, exchange: str):
    with _lock:
        market_prices[f"{exchange}:{symbol}"] = {
            "symbol": symbol,
            "exchange": exchange,
            "bid": float(bid),
            "ask": float(ask),
        }


def get_prices_snapshot():
    with _lock:
        return dict(market_prices)
