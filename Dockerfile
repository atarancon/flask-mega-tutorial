FROM python:3.8.0-slim

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

# create directory for the app user
ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH
 
# create the app user
RUN useradd -ms  /bin/bash  app


COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
#professional lint checking 
RUN pip install flake8
RUN pip install sqlalchemy-utils
RUN pip install -r requirements.txt

COPY . .

RUN pip install --editable .


# chown all the files to the app user
RUN chown -R app:app $INSTALL_PATH

# change to the app user
USER app

ENV PORT=8000
# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			

CMD gunicorn --bind 0.0.0.0:$PORT  "app.app:create_app('config.setting.ProdConfig')"
 

 


