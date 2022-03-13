
#!/bin/bash

/usr/local/bin/aws configure set aws_access_key_id $ACCESS_KEY_ID
/usr/local/bin/aws configure set aws_secret_access_key $SECRET_ACCESS_KEY
/usr/local/bin/aws configure set default.region us-east-1

python3 ./python/main.py $FILE_URI