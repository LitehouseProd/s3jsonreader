import subprocess;
import json;
from getCreds import getFile;


def getLocation(url):
    source=url.split('/')
    return source

def get_all_keys(info):
    print("get_all_keys?")
    for key, value in info.items():
            yield key
            print(key)
            if key == 'message':
                print("if")
                print(info['message'])
            elif isinstance(value, dict):
                print("elif")
                yield from get_all_keys(value)

def readFile(fileLocation):
    with open(fileLocation, "r") as read_file:
        data = json.load(read_file)
        print("file is read")
        return data
        

sourceArray = getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test2.json')
file = getFile(sourceArray[2], sourceArray[3])
contents = readFile(file)
print("got data")
get_all_keys(contents)
print("got keys")