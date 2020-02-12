from pymongo import MongoClient

client = MongoClient("mongodb://localhost/companies")
db = client.get_database()

def queryLocation(parameter,collection,maxDistance=2000,minDistance=0,field="location"):
    '''Genera una geoquery para comprobar qué documentos cumplen con las características
       requeridas'''
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
    '''Devuelve el número de resultados de la geoquery
       en forma de lista'''
    matches = []
    for i in range(len(parameter)):
        check = queryLocation(parameter[i],collection)
        matches.append(len(check))
    return matches