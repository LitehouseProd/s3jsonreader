from s3Reader import getAllinfo, readFile, getLocation;
import getCreds;
import pytest;
import json

def testread():
    with open('../jsonfile/test.json','r') as readfile:
        data = json.load(readfile)
        assert getAllinfo(data) == 'Hello, World!'
    
def testRead2():
    with open('../jsonfile/test2.json','r') as readfile:
        data = json.load(readfile)
        assert getAllinfo(data) == 'Hello, World!'

def testLoad():
    with open('../jsonfile/test.json','r') as readfile:
        data = json.load(readfile)
        assert readFile('../jsonfile/test.json') == data

def testLoad2():
    with open('../jsonfile/test2.json','r') as readfile:
        data = json.load(readfile)
        assert readFile('../jsonfile/test2.json') == data