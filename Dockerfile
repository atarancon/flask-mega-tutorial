FROM python:3.8.0-slim

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
#professional lint checking 
RUN pip install flake8
RUN pip install sqlalchemy-utils
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable . 
#RUN flake8 app

#CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app.app:create_app('config.setting.DevConfig')"
