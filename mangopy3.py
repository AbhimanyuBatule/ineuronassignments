import pymongo
client = pymongo.MongoClient("mongodb+srv://Abhimanyu:abhimanyu95@cluster0.ay2s6j1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collection = database["table"]
#collection.insert_many(data)
#d = collection.find({'status':'A'})
#d = collection.find({'status':{'$in':['A' , 'P']}})
#d = collection.find({'status':{"$gt" : "C"}})
#d = collection.find({'qty':{'$gte' :75}})
#d = collection.find({'item': 'sketch pad','qty': 95})
#d = collection.find({ 'item': 'sketch pad' , 'qty' :{"$gte" : 75}})
#d = collection.find({'$or' : [{ 'item': 'sketch pad'} , {'qty': {"$gte": 75}}]})
#collection.update_one({'item': 'canvas'} , {'$set':{'item': 'Abhi'} })
collection.delete_one({'item': 'Abhi'})
d = collection.find({'item': 'Abhi'})
for i in d :
    print(i)