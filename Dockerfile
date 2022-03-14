FROM python:latest
WORKDIR /application
RUN pip install awscli
COPY ./python/s3reader.py s3reader.py
COPY ./python/main.py main.py
COPY ./python/getCreds.py getCreds.py
COPY ./python/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY entry.sh entrypoint.sh
RUN chmod +x entrypoint.sh
RUN chmod 777 entrypoint.sh
RUN chown circleci. entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]