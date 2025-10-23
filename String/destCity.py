def destCity(paths):
    sources = {a for a, _ in paths}
    destionations = {b for _, b in paths}

    # true start point only includes in sources
    # true destination only includes in destionations
    for city in destionations:
        if city not in sources:
            return city

paths = [["B","C"],["D","B"],["C","A"]]
print(destCity(paths))