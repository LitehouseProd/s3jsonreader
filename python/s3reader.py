import subprocess;
import json;
from getCreds import getFile;


def getLocation(url):
    source=url.split('/')
    return source

def readFile(fileLocation):
    with open(fileLocation, "r") as read_file:
        data = json.load(read_file)
        # for i in data.items():
        #     if type(i) is dict:
        #         for j in i.items():
        #             if j is 'message':
        #                 print(j['message'])
        print(data['message'])

sourceArray = getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test.json')
file = getFile(sourceArray[2], sourceArray[3])
readFile(file)
