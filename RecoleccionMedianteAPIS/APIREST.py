import requests

URL = 'http://maps.googleapis.com/maps/api/directions/json'
params = dict(
    origin='Bogota,Colombia',
    destination='Medellin,Colombia',
    mode='driving'
)

resp = requests.get(url=URL, params=params)

data = resp.json()

print(
    data['routes'][0]['legs'][0]['duration']['text']
)