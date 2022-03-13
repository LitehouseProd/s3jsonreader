import subprocess;
import sys, getopt
import json;
from getCreds import getFile;


def getLocation(url):
    source=url.split('/')
    return source

def readFile(fileLocation):
    with open(fileLocation, "r") as read_file:
        data = json.load(read_file)
        return data

def getAllkeys(info):
    for key, value in info.items():
        if key == 'message':
            return(value)
        elif isinstance(value, dict):
            return getAllkeys(value)

sourceFile = sys.argv[1]
sourceArray = getLocation(sourceFile)
file = getFile(sourceArray[2], sourceArray[3])
data = readFile(file)
message = getAllkeys(data)
print(message)