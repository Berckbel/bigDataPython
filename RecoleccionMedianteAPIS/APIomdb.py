import requests

clave = '3e91b370'
uri = 'http://www.omdbapi.com/?apikey=' + clave

r = requests.get(uri, {
    's' : 'The Matrix',
    'type' : 'movie'
})

print(r.json())

r = requests.get(uri, {
    'i' : 'tt0133093'
})

print('---------------------------------------------------------------------------------------------------')

print(r.json())

