from fastapi import FastAPI

app = FastAPI(title="Triangular Arbitrage Bot API")

stats = {
    "status": "running",
    "profit": 0.0,
    "trades": 0,
    "prices_count": 0,
    "exchange_1": "binance",
    "exchange_2": "bybit",
    "last_opportunity": None,
}


@app.get("/")
def root():
    return {"message": "Triangular Arbitrage Bot API"}


@app.get("/health")
def health():
    return {"ok": True, "status": "running"}


@app.get("/stats")
def get_stats():
    return stats