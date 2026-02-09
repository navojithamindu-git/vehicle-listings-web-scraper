from openpyxl import Workbook
from pymongo import MongoClient


def save_to_excel(data, filename="scraped_vehicles.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Vehicle Listings"

    ws.append(["Vehicle", "Place", "Price", "Mileage", "Time", "URL"])

    for item in data:
        ws.append([
            item["vehicle"],
            item["place"],
            item["price"],
            item["mileage"],
            item["time"],
            item["url"]
        ])

    wb.save(filename)


def save_to_mongodb(data, db_name="VehicleData", collection_name="details"):
    client = MongoClient("mongodb://localhost:27017")
    db = client[db_name]
    collection = db[collection_name]

    if data:
        collection.insert_many(data)
