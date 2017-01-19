FROM training/webapp
RUN apt-get -y update && apt-get -y install libpq-dev python-dev
RUN pip install pygresql # pygresql lets python scripts talk to PostgreSQL
ADD app.py /opt/webapp/app.py