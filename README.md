## Triangular Arbitrage Bot

Triangular arbitrage monitoring bot for Binance and Bybit.

The project includes:

- FastAPI backend
- WebSocket market data
- Arbitrage engine
- Web dashboard
- Docker deployment

---

# Project Structure

backend/
    exchanges/      # Binance and Bybit clients
    engine/         # arbitrage logic
    market/         # websocket price feeds
    services/       # telegram and helpers
    api/            # FastAPI server
    main.py

frontend/
    index.html
    style.css
    dashboard.js

Dockerfile
docker-compose.yml

---

# Environment Variables

Create `.env` file based on `.env.example`

Example:

BINANCE_KEY=
BINANCE_SECRET=

BYBIT_KEY=
BYBIT_SECRET=

TELEGRAM_TOKEN=
TELEGRAM_CHAT=

TRADE_SIZE=50
MIN_PROFIT=0.003

---

# Run With Docker

Build and start the project:

```bash
docker-compose up --build