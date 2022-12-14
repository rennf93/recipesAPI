# We use this particular python version because it's very strict, 
# is minimal and it goes great hand in hand with Linux.
FROM python:3.9-alpine3.13
LABEL maintainer="https://www.linkedin.com/in/renzo-f/"

# We tell Python that we don't want to buffer the output.
# Prints directly on console and avoid delays.
ENV PYTHONUNBUFFERED 1

# COPY the requirements into the docker image.
COPY ./requirements.txt /tmp/requirements.txt

# COPY the requirements into the docker image - DEV ENV
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# COPY the app's director into the docker image.
COPY ./app /app

# We set the working directory, where commands run from.
# Automatically runs them from the following directory.
WORKDIR /app

# Allows us to acces through that port to the container.
EXPOSE 8000

# Set true for DEV ENV, false for PROD ENV
ARG DEV=false

# We give the commands we need to run.
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
    -D \
    -H \
    renzof

# Update PATH environment variable.
ENV PATH="/py/bin:$PATH"

# We specify the user that we're switching to.
USER renzof