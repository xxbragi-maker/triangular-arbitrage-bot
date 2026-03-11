from fastapi import FastAPI

app = FastAPI(title="Triangular Arbitrage Bot API")

stats = {
    "status": "starting",
    "profit": 0.0,
    "trades": 0,
    "prices_count": 0,
    "exchange_1": "binance",
    "exchange_2": "bybit",
    "last_opportunity": None,
}


@app.on_event("startup")
def on_startup():
    from backend.main import start_engine

    start_engine()
    stats["status"] = "running"


@app.get("/")
def root():
    return {"message": "Triangular Arbitrage Bot API"}


@app.get("/health")
def health():
    return {"ok": True, "status": stats["status"]}


@app.get("/stats")
def get_stats():
    return stats