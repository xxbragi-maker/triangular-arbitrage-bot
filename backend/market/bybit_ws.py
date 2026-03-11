import asyncio
import json
import websockets

from backend.market.cache import update_price

BYBIT_WS_URL = "wss://stream.bybit.com/v5/public/spot"
BYBIT_TOPICS = [
    "tickers.BTCUSDT",
    "tickers.ETHBTC",
    "tickers.ETHUSDT",
]


def normalize_symbol(symbol: str) -> str:
    mapping = {
        "BTCUSDT": "BTC/USDT",
        "ETHBTC": "ETH/BTC",
        "ETHUSDT": "ETH/USDT",
    }
    return mapping.get(symbol, symbol)


async def run_bybit_ws():
    while True:
        try:
            async with websockets.connect(BYBIT_WS_URL, ping_interval=20, ping_timeout=20) as ws:
                await ws.send(json.dumps({
                    "op": "subscribe",
                    "args": BYBIT_TOPICS
                }))

                while True:
                    message = await ws.recv()
                    data = json.loads(message)

                    if data.get("topic", "").startswith("tickers.") and "data" in data:
                        payload = data["data"]
                        symbol = payload.get("symbol")
                        bid = payload.get("bid1Price")
                        ask = payload.get("ask1Price")

                        if symbol and bid and ask:
                            update_price(normalize_symbol(symbol), float(bid), float(ask), "bybit")
        except Exception as e:
            print("Bybit WS error:", str(e))
            await asyncio.sleep(5)
