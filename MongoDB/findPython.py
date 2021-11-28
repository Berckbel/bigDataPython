from pymongo import MongoClient

client = MongoClient('mongodb://localhost:28000/')

db = client['twitter']
tweets = db['tweets']


tweet = tweets.find_one({'usuario.nick':'bertoldo'},{'text':1, '_id':0})

print(tweet)

tweet = tweets.find_one({'usuario.nick':'bertoldo'})

print('text: ', tweet['text'])

for t in tweets.find({'usuario.nick':'bertoldo','mentions':'herminia'}):
    print(t['text'])

