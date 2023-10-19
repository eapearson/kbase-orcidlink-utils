FROM python:3.12.0-alpine3.18

RUN mkdir -p /app && chmod -R a+rw /app && apk add bash

COPY ./entrypoint.sh /app
COPY ./requirements.txt /app
COPY ./src /app/src

WORKDIR "/app"

RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]

# If you don't run the image with a command, it drops into bash.
CMD ["bash"]
