FROM python:3.9.1-alpine3.12

ARG APP_PORT=8000
ENV APP_PORT=$APP_PORT
ENV ROOT_DIR /my_app
WORKDIR $ROOT_DIR

ENV PYTHONDONTWRITEBYTECODE 1 # prevents from writing pyc files to the disc
ENV PYTHONUNBUFFERED 1 # prevents from buffering stdout and stderr

# install psycopg2 dependencies
RUN apk update \
  && apk add postgresql-dev gcc python3-dev musl-dev curl \
  && rm -rf /var/cache/apk/* /var/lib/apt/lists/*

# install dependencies
COPY Pipfile Pipfile.lock $ROOT_DIR/
RUN pip install --upgrade pip \
  && pip install pip install pipenv \
  && pipenv install --system --deploy --ignore-pipfile \
  && rm -rf ~/.cache/pip

# define healthcheck
HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl --fail "http://localhost:$APP_PORT/healthcheck/" || exit 1

# running server
CMD sh -c "python manage.py runserver 0.0.0.0:$APP_PORT"

