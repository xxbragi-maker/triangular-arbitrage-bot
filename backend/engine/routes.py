def generate_routes(symbols):
    routes = []

    for a in symbols:
        for b in symbols:
            for c in symbols:
                if a != b and b != c and a != c:
                    routes.append((a, b, c))

    return routes
