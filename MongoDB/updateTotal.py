from pymongo import MongoClient
client = MongoClient('mongodb://localhost:28000/')
db = client['astronomia']
estelar = db['estelar']

estelar.drop()
estelar.insert_many([
    {'_id':1,'nombre':"Sirio",'tipo':"estrella",'espectro':"A1V"},
    {'_id':2,'nombre':"Saturno",'tipo':"planeta"},
    {'_id':3,'nombre':"Pluton",'tipo':"planeta"}
])

pluton = estelar.find_one({'_id':3})
pluton['tipo'] = "planeta_enano"
estelar.replace_one({'_id':pluton['_id']},pluton)