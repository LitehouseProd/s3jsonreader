import sys
from s3reader import getAllkeys, readFile, getLocation;
from getCreds import getFile;

sourceFile = sys.argv[1]
sourceArray = getLocation(sourceFile)
file = getFile(sourceArray[2], sourceArray[3])
data = readFile(file)
message = getAllkeys(data)
print(message)
