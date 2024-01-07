FROM python:3.9.1-alpine3.12

ENV ROOT_DIR /my_app
WORKDIR $ROOT_DIR

ENV PYTHONDONTWRITEBYTECODE 1 # prevents from writing pyc files to the disc
ENV PYTHONUNBUFFERED 1 # prevents from buffering stdout and stderr

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# start script
COPY ./entrypoint .

COPY . .

ENTRYPOINT ["/my_app/entrypoint"]