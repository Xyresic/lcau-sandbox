import json

with open('cities_raw.txt', 'r') as f:
    cities = {line.strip(): set() for line in f.readlines()}

with open('cities_raw_full.txt', 'r') as f:
    cities_full = [line.strip().split(', ') for line in f.readlines()]

for city in cities_full:
    key = ', '.join(city[:-1])
    if key in cities:
        cities[key].add(city[-1])

cities = {city: {'docs': sorted(list(docs))} for city, docs in cities.items()}
with open('serialized.js', 'r') as f:
    locations = eval(f.read()[16:-1].replace('`', '"'))

new_locations = []
for location in locations:
    key = location[2]
    if key in cities:
        cities[key]['lat'] = location[0]
        cities[key]['long'] = location[1]
        new_locations.append(tuple(location))

with open('cities.json', 'w') as f:
    json.dump(cities, f, indent=2)

with open('serialized.js', 'w') as f:
    f.write(f'let locations = [{", ".join([f"[{lat}, {long}, `{city}`]" for lat, long, city in new_locations])}];')
