import json;


def getLocation(url):
    source=url.split('/')
    return source

def readFile(fileLocation):
    with open(fileLocation, "r") as read_file:
        data = json.load(read_file)
        return data

def getAllkeys(info):
    for key, value in info.items():
        print(key)
        if key == 'message':
            return("Hello")
        elif isinstance(value, dict):
            return getAllkeys(value)

