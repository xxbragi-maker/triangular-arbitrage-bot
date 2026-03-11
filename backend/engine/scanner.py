def scan_routes(routes, prices):
    opportunities = []

    for route in routes:
        p1 = prices.get(route[0], 1)
        p2 = prices.get(route[1], 1)
        p3 = prices.get(route[2], 1)

        result = p1 * p2 * p3

        if result > 1.003:
            opportunities.append({
                "route": route,
                "profit": result
            })

    return opportunities
