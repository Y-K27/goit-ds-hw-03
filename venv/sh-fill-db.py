from pymongo import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse 

username = urllib.parse.quote_plus('username')  
password = urllib.parse.quote_plus('password')
cluster_name = "claster"

url = f"mongodb+srv://{username}:{password}@{cluster_name}.mrx0mbn.mongodb.net/?retryWrites=true&w=majority&appName={cluster_name}"

client = MongoClient(
    url,
    server_api=ServerApi('1')
)

db = client.book

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
        {
            "name": "barsik",
            "age": 3,
            "features": ["ходить в капці", "дає себе гладити", "рудий"],
        },
    ]
)
print(result_many.inserted_ids)

