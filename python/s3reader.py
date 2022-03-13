import subprocess;
import json;
from getCreds import getFile;


def getLocation(url):
    source=url.split('/')
    return source

def get_all_keys(Dict):
    for key, value in Dict.items():
            yield key
            if isinstance(value, dict):
                yield from get_all_keys(value)

def readFile(fileLocation):
    with open(fileLocation, "r") as read_file:
        data = json.load(read_file)
        for i in get_all_keys(data):
            if i == 'message':
                print(i)
        

sourceArray = getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test2.json')
file = getFile(sourceArray[2], sourceArray[3])
readFile(file)
