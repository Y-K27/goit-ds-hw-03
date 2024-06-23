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

def print_all_records(): #функція виводить всі записи з бази даних
    result = db.cats.find({})
    for el in result:
        print(el)

def print_rebor_by_name(cats_name:str):             #функція виводить запис з бази даних за заданим ім'ям
    result = db.cats.find_one({"name": cats_name})
    return result
#функція оновлює вік в базі даних за заним іменем 
def update_information_of_age(cat_name:str, cat_age:int):
    db.cats.update_one({"name": cat_name}, {"$set": {"age": cat_age}})
    result = db.cats.find_one({"name":cat_name})
    return result

#функція оновлює опис в базі даних за заним іменем 
def update_information_of_features(cat_name:str, cat_features:list):
    db.cats.update_one({"name": cat_name}, {"$set": {"features": cat_features}})    #перелік характеристик подається списком наприклад:["ходить в лоток", "не дає себе гладити", "сірий"]
    result = db.cats.find_one({"name": cat_name})
    return result

#функція видаляє запис з заним іменем із бази даних
def delete_record_by_name(cat_name:str):
    db.cats.delete_one({"name": cat_name})
    return f"Record with name:{cat_name} - deleted"

#функція видаляє всі записи з таблиці(файлу) бази даних
def delete_all_record():
    db.cats.delete_many({})
    return "All record was deleted"


