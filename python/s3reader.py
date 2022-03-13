import boto3;
import json;
from getCreds import get_secret;

s3 = boto3.resource('s3')

def getFile(Bucket, file):
    s3.Object(Bucket, file).downloadfile('/tmp/test.json')

def getLocation(url):
    source=url.split('/')
    return source

sourceArray = getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test.json')
getFile(sourceArray[2], sourceArray[3])
