import os
import pgdb

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    conn = pgdb.connect( host='pg', user='postgres', password='testnet', database='testnet' )
    cur = conn.cursor()
    cur.execute( "SELECT value FROM kv WHERE key='provider'" )
    provider = cur.fetchone()[0]
    conn.close()
    return 'Hello '+provider+'!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)