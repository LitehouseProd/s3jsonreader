from s3reader import getAllkeys, readFile, getLocation;
import getCreds;
import pytest;
import json

def testread():
    with open('../jsonfile/test.json','r') as readfile:
        data = json.load(readfile)
        assert getAllkeys(data) == 'Hello, World!'
    
def testRead2():
    with open('../jsonfile/test2.json','r') as readfile:
        data = json.load(readfile)
        assert getAllkeys(data) == 'Hello, World!'

def testLoad():
    with open('../jsonfile/test.json','r') as readfile:
        data = json.load(readfile)
        assert readFile('../jsonfile/test.json') == data

def testLoad2():
    with open('../jsonfile/test2.json','r') as readfile:
        data = json.load(readfile)
        assert readFile('../jsonfile/test2.json') == data

def testURLParse():
    assert getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test2.json') == ['s3:', '', 'ecr-test-fiftheyeecrtest-1cc7embghgf27', 'test2.json']