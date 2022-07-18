FROM python:3.10.5-alpine

COPY ./docker/backend/start /start
RUN chmod +x /start

# Install python packages
COPY ./requirements/requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /src/backend

ENTRYPOINT [""]