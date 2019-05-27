import os
import pgdb
import logging
import sys

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    try: 
        conn = pgdb.connect( host='database', user='postgres', password='myPassword', database='mydata' )
        cur = conn.cursor()
        cur.execute( "SELECT value FROM kv WHERE key='provider'" )
        provider = cur.fetchone()[0]
        conn.close()
        return 'Hello '+provider+'!'
    except: # catch *all* exceptions
        return '<h1>An error occurred:</h1> ' + str(sys.exc_info()[1]) + '<br/><h3>Check the following:</h3> <li>Which password is set on the database container? <li>Is your database container named "database"? <li>Is the data created correctly in the database?'

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
