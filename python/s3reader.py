import subprocess;
import json;
from getCreds import getFile;


def getLocation(url):
    source=url.split('/')
    return source

def readFile(fileLocation):
    with open(fileLocation, "r") as read_file:
        data = json.load(read_file)
        print("file is read")
        return data

def getAllkeys(info):
    print("get_all_keys?")
    for key, value in info.items():
        print(key)
        if key == 'message':
            print("if")
            print(value)
        elif isinstance(value, dict):
            print("elif")
            yield from getAllkeys(value)
        

sourceArray = getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test2.json')
file = getFile(sourceArray[2], sourceArray[3])
contents = readFile(file)
print("got data")
getAllkeys(contents)
print("got keys")