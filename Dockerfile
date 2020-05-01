FROM python:3

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

WORKDIR /flasktasklist

COPY app /flasktasklist/

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app:app"