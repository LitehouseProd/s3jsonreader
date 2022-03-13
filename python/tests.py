from s3reader import getAllkeys, readFile, getLocation;
import pytest;
import json
import os

file1 = os.path.join(os.path.dirname(__file__), 'jsonfile/test.json')
file2 = os.path.join(os.path.dirname(__file__), 'jsonfile/test2.json')

def testread():
    with open(file1,'r') as readfile:
        data = json.load(readfile)
        assert getAllkeys(data) == 'Hello, World!'
    
def testRead2():
    with open(file2,'r') as readfile:
        data = json.load(readfile)
        assert getAllkeys(data) == 'Hello, World!'

def testLoad():
    with open(file1,'r') as readfile:
        data = json.load(readfile)
        assert readFile(file1) == data

def testLoad2():
    with open(file2,'r') as readfile:
        data = json.load(readfile)
        assert readFile(file2) == data

def testURLParse():
    assert getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test2.json') == ['s3:', '', 'ecr-test-fiftheyeecrtest-1cc7embghgf27', 'test2.json']