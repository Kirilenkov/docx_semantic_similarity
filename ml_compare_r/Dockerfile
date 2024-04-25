FROM python:3
ENV PYTHONUNBUFFERED 1
COPY . ./
COPY requirements.txt ./
WORKDIR /
RUN pip3 install -r requirements.txt --no-cache-dir
RUN apt update
RUN apt install -y sqlite3 libsqlite3-dev
RUN python manage.py migrate
