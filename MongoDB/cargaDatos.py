from pymongo import MongoClient

client = MongoClient('mongodb://localhost:28000/')

db = client['twitter']
tweets = db['tweets']

tweet = {
    '_id': 2,
    'usuario': {'nick':"herminia",'seguidores':5320},
    'texto': "RT:@herminia: hoy, excursion a la sierra con @aniceto",
    'menciones': ["herminia","aniceto"],
    'RT': True,
    'origen': 1
}

insertado = db.tweets.insert_one(tweet)
print(insertado.inserted_id)