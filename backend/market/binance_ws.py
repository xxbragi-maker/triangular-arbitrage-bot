import asyncio
import json
import websockets

from backend.market.cache import update_price

BINANCE_STREAMS = [
    "btcusdt@bookTicker",
    "ethbtc@bookTicker",
    "ethusdt@bookTicker",
]

BINANCE_WS_URL = (
    "wss://data-stream.binance.vision/stream?streams="
    + "/".join(BINANCE_STREAMS)
)


async def run_binance_ws():
    while True:
        try:
            async with websockets.connect(BINANCE_WS_URL, ping_interval=20, ping_timeout=20) as ws:
                while True:
                    message = await ws.recv()
                    data = json.loads(message)

                    payload = data.get("data", {})
                    symbol = payload.get("s")
                    bid = payload.get("b")
                    ask = payload.get("a")

                    if symbol and bid and ask:
                        normalized = symbol.replace("USDT", "/USDT").replace("BTC", "/BTC")
                        if normalized.count("/") > 1:
                            if symbol == "ETHBTC":
                                normalized = "ETH/BTC"
                            elif symbol == "BTCUSDT":
                                normalized = "BTC/USDT"
                            elif symbol == "ETHUSDT":
                                normalized = "ETH/USDT"

                        update_price(normalized, float(bid), float(ask), "binance")
        except Exception as e:
            print("Binance WS error:", str(e))
            await asyncio.sleep(5)
