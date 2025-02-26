from pymongo import MongoClient

# connessione al server
client = MongoClient("mongodb://localhost:27017")
db = client.provamongo

print(client.server_info())

# inserire nuovo documento
collection = db.utenti
utenti = [
    {
        "nome": "Giuseppe",
        "cognome": "Verdi"
    },
    {
        "nome": "Luca",
        "cognome": "Bianchi",
        "eta": 30,
        "occupazione": "data engineer"
    },
    {
        "nome": "Alice",
        "cognome": "Rossi",
        "eta": 25,
        "gatti": ["Arthur", "Silver"]
    }
]

result = collection.insert_many(utenti)
print(result.inserted_ids)



