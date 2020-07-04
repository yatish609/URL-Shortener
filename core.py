import pymongo,dns, requests
import hashid_gen

client = pymongo.MongoClient("mongodb+srv://pu:pu@cluster0.flv2q.mongodb.net/urldb?retryWrites=true&w=majority")
db = client.urldb
url_collection = db.url

# Unique code size
idgen = hashid_gen.IDGenerator(8)

def createURL():
    short_url = "www.xyz.com/" + str(idgen.generate_id())
    return str(short_url)

def checkifexists(original_url):
    if(url_collection.find_one({'url': original_url})):
        print('found true')
        return True
    print('found false, inserting data..')
    return False

def checkifshortexists(short_url):
    if(url_collection.find_one({'short_url': short_url})):
        print('found true')
        return True
    print('found false, inserting data..')
    return False

def updatedb(original_url, short_url):
    post = {'url': original_url, 'short_url': short_url}
    url_collection.insert_one(post)

def uri_exists_stream(uri: str) -> bool:
    try:
        with requests.get(uri, stream=True) as response:
            try:
                response.raise_for_status()
                return True
            except requests.exceptions.HTTPError:
                return False
    except requests.exceptions.ConnectionError:
        return False