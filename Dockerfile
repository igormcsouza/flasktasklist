FROM python:3

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

WORKDIR /flasktasklist

COPY app /flasktasklist/app

ENTRYPOINT ["python3", "app/app.py"]