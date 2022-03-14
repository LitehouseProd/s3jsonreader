FROM cimg/python:3.10.2
WORKDIR /application
RUN pip install awscli
COPY ./python/s3reader.py python/s3reader.py
COPY ./python/main.py python/main.py
COPY ./python/getCreds.py python/getCreds.py
COPY ./python/requirements.txt python/requirements.txt
RUN pip install -r python/requirements.txt
COPY entry.sh entrypoint.sh
USER root
RUN chmod +x entrypoint.sh
RUN chmod 777 entrypoint.sh
RUN chown circleci. entrypoint.sh
USER circleci

ENTRYPOINT ["aws configure set aws_access_key_id $ACCESS_KEY_ID && \
aws configure set aws_secret_access_key $SECRET_ACCESS_KEY && \
aws configure set default.region us-east-1 && \
python3 ./python/main.py $FILE_URI"]