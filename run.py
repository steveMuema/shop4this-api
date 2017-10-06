import os
import urlparse
import psycopg2
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='thisismysecret'

urlparse.uses_netloc.append('posgres')
url = urlparse.urlparse(os.environ['DATABASE_URI'])

db = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.host,
    port=url.port
)

if __name__ == '__main__':
    app.run(debug=True)