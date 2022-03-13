FROM cimg/python:3.10.2
WORKDIR /application
RUN pip install awscli
COPY ./python python
RUN pip install -r python/requirements.txt
COPY entrypoint.sh entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]