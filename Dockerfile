FROM python:3.13.0b1-slim

ARG PORT_DEFAULT=8000
ENV PORT=$PORT_DEFAULT

ARG HOST_ACCEPT_CONNECTION_FROM_OUTSIDE=0.0.0.0
ENV HOST=$HOST_ACCEPT_CONNECTION_FROM_OUTSIDE

WORKDIR /app

RUN mkdir modules

COPY Pipfile Pipfile.lock .launch_api_server ./
COPY modules /app/modules/

RUN pip install --no-cache-dir pipenv && \
    python -m pip install --upgrade pip && \
    pipenv install --system --deploy && \
    echo '#!/usr/bin/env bash' > /app/start_api_server && \
    echo 'uvicorn modules.api.berlin_clock:app --host ${HOST} --port ${PORT}' >> /app/start_api_server && \
    chmod 755 /app/start_api_server

EXPOSE $PORT

ENTRYPOINT ["/app/start_api_server"]
