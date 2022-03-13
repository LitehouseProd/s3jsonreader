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
        getAllkeys(data)

def getAllkeys(info):
    for key, value in info.items():
        if key == 'message':
            print(value)
        elif isinstance(value, dict):
            return getAllkeys(value)

def input():
    try:
        args = getopt.getopt(argv)
    except getopt.GetoptError:
        print('s3readert.py <S3 URI>')
    return args    


sourceFile = input()
sourceArray = getLocation(sourceFile)
file = getFile(sourceArray[2], sourceArray[3])
readFile(file)