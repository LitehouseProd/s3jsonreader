
#!/bin/bash

aws configure set aws_access_key_id $ACCESS_KEY_ID
aws configure set aws_secret_access_key $SECRET_ACCESS_KEY
aws configure set default.region us-east-1
echo $FILE_URI
python3 main.py $FILE_URI
