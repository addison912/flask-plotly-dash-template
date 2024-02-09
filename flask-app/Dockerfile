FROM ubuntu:20.04


RUN apt-get update -y && \
    apt-get install -y python3-pip

ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=developement

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "wsgi.py" ]