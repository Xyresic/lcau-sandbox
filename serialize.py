import geopy.geocoders
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

geopy.geocoders.options.default_timeout = None
geolocator = Nominatim(user_agent='ericlam@mit.edu')
geocoder = RateLimiter(geolocator.geocode, min_delay_seconds=2, max_retries=5)

with open('cities_raw.txt', 'r') as f:
    cities = [c.strip() for c in f.readlines()]
    locations = [(l.latitude, l.longitude) for l in [geocoder(c) for c in cities] if l is not None]

with open('serialized.js', 'w') as f:
    f.write(f'let locations = [{", ".join([f"[{lat}, {long}]" for lat, long in locations])}];')
