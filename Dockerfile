FROM python:3-slim AS build-env
WORKDIR /app
COPY heartbeat heartbeat
COPY requirements.txt requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]

##################################################

FROM python:3.6.5-alpine
COPY --from=build-env /app /app
COPY --from=build-env /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=build-env /usr/local/bin/gunicorn /usr/local/bin/gunicorn
WORKDIR /app
EXPOSE 5000
CMD ["gunicorn", "--pythonpath=heartbeat", "--worker-class=eventlet", "--bind=0.0.0.0:5000", "wsgi:app"]
