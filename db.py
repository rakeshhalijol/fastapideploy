import pymongo
mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["STUDENTSDB"]
collection = db["students"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return response.inserted_id

def get_all():
    responses = collection.find({})
    data = []
    for response in responses:
        response["_id"] = str(response["_id"]) 
        data.append(response)
    return data