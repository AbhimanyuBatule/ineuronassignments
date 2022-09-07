import pymongo
client = pymongo.MongoClient("mongodb+srv://Abhimanyu:abhimanyu95@cluster0.ay2s6j1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name": "abhimanyu",
    "email":"abhibatule@gmail.com",
    "subject" : ["maths", "English","Science", "History"]
}
database = client['mango1']
collections = database["Abhi"]
collections.insert_one(d)

record = collections.find()
for i in record:
    print(i)