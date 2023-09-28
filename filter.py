with open('cities_raw.txt', 'r') as f:
    cities = f.readlines()
    cities.sort()

with open('cities_raw.txt', 'w') as f:
    f.write(''.join(cities))
