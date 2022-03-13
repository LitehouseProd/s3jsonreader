FROM cimg/python:3.10.2
WORKDIR /application
RUN pip install awscli
COPY ./python/s3reader.py python/s3reader.py
COPY ./python/main.py python/main.py
COPY ./python/getCreds.py python/getCreds.py
COPY ./python/requirements.txt python/requirements.txt
RUN pip install -r python/requirements.txt
COPY entrypoint.sh entrypoint.sh
USER root
RUN chmod +X ./entrypoint.sh
RUN chmod 777 ./entrypoint.sh
USER circleci

ENTRYPOINT ["./entrypoint.sh"]