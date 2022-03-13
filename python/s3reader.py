import boto3;
import subprocess;
import json;
from getCreds import getFile;


def getLocation(url):
    source=url.split('/')
    return source

sourceArray = getLocation('s3://ecr-test-fiftheyeecrtest-1cc7embghgf27/test.json')
getFile(sourceArray[2], sourceArray[3])
subprocess.run(["ls", "/tmp"])