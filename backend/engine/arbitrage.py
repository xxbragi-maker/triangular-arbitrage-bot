from backend.engine.routes import generate_routes
from backend.engine.scanner import scan_routes


def find_arbitrage(symbols, prices):
    routes = generate_routes(symbols)
    opportunities = scan_routes(routes, prices)
    return opportunities
