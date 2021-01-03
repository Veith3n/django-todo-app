FROM python:3.9.1-alpine3.12

WORKDIR /my_app

ENV PYTHONDONTWRITEBYTECODE 1 # prevents from writing yc files to the disc
ENV PYTHONUNBUFFERED 1 # prevents from buffering stdout and stderr

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .