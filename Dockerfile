FROM python:3.9-slim

ARG PORT_DEFAULT=8000
ENV PORT=$PORT_DEFAULT

ARG HOST_ACCEPT_CONNECTION_FROM_OUTSIDE=0.0.0.0
ENV HOST=$HOST_ACCEPT_CONNECTION_FROM_OUTSIDE

WORKDIR /app

RUN mkdir modules

COPY Pipfile Pipfile.lock .launch_api_server ./
COPY modules /app/modules/

RUN pip install --no-cache-dir  pipenv && \
    pipenv install --system --deploy

EXPOSE $PORT

ENTRYPOINT uvicorn modules.api.berlin_clock:app --host ${HOST} --port ${PORT}