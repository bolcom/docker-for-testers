FROM training/webapp
RUN apt-get -y update && apt-get -y install libpq-dev python-dev
RUN pip install pygresql
ADD app.py /opt/webapp/app.py