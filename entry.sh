
#!/bin/bash

FILE_URI=$1
ACCESS_KEY_ID=$2
SECRET_ACCESS_KEY=$3

aws configure set aws_access_key_id $ACCESS_KEY_ID
aws configure set aws_secret_access_key $SECRET_ACCESS_KEY
aws configure set default.region us-east-1

python3 main.py $FILE_URI
