import tweepy
import json

ruta = 'BigDataPythonSolucionario\Cap1\Busqueda_puntual.json'
ruta_datos = 'BigDataPythonSolucionario\Cap1\Busqueda_streaming.json'

CONSUMER_TOKEN = 'ViJfmnHlMqRcsQCLAgYiiK6gx'
CONSUMER_SECRET = 'g4Nv7ZOZWoxdSpEzqrPTytcNpMcm9gnQtFMWaHit66ZO94eI8K'
ACCESS_TOKEN = '3885340353-91hSyiO78jFKBacwxEAExPTM1UCFYQlXlb96Ism'
ACCESS_TOKEN_SECRET = 'AxC9dSJ87j1UdcTsXLIVsc2AXW8RsBGHvWLay7S2Do0u2'

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

lista_tweets = api.search(q='python')
lista_json = []
for tweet in lista_tweets:
    lista_json.append(tweet._json)

with open(ruta, 'w', encoding='utf-8') as fich_escr:
    json.dump(lista_json, fich_escr, ensure_ascii=False, indent=4)

class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api, ruta):
        super().__init__(api)
        self.fich = open(ruta, 'a')
    
    def on_status(self, status):
        self.fich.write(json.dumps(status._json) + '\n')
    
    def on_error(self, status_code):
        self.fich.close

myStreamListener = MyStreamListener(api,ruta_datos)
flujo = tweepy.Stream(auth=auth, listener=myStreamListener)
flujo.filter(track=['python'])