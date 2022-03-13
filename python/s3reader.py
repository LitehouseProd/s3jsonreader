import subprocess;
import json;
from getCreds import getFile;


def getLocation(url):
    source=url.split('/')
    return source

def readFile(fileLocation):
    with open(fileLocation, "r") as read_file:
        data = json.load(read_file)
        getAllkeys(data)

def getAllkeys(info):
    for key, value in info.items():
        if key == 'message':
            print(value)
        elif isinstance(value, dict):
            return getAllkeys(value)
        

sourceArray = getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test2.json')
file = getFile(sourceArray[2], sourceArray[3])
readFile(file)