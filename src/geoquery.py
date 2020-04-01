from pymongo import MongoClient

client = MongoClient("mongodb://localhost/companies")
db = client.get_database()

def queryLocation(parameter,collection,maxDistance=1500,minDistance=0,field="location"):
   '''Makes qeoqueries in MongoDB to find out wich documents matches with specified requirements'''
   return list(db[collection].find({
      field: {
         "$near": {
         "$geometry": parameter,
         "$maxDistance": maxDistance,
         "$minDistance": minDistance
         }
      }
   }
   )
   )

def geoquery(parameter,collection):
   '''Returns the number of matches'''
   matches = []
   for i in range(len(parameter)):
      check = queryLocation(parameter[i],collection)
      matches.append(len(check))
   return matches