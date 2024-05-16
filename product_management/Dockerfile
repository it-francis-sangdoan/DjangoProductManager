FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app 

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000