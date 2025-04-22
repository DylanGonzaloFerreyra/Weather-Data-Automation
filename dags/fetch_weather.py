import requests
import pymongo
from datetime import datetime

MONGO_URI = "mongodb://localhost:27017"
client = pymongo.MongoClient(MONGO_URI)
db = client.weatherDB
collection = db.weather

API_KEY = ""  
CITY = "Buenos Aires"  
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_and_store_weather():
    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "timestamp": datetime.now()
        }
        collection.insert_one(weather_data)
        print("Datos almacenados:", weather_data)
    else:
        print("Error al obtener datos:", data)

if __name__ == "__main__":
    fetch_and_store_weather()