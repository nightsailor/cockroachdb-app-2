from sqlalchemy import create_engine
import urllib
import os
from decouple import config

def connect(db_uri):
    engine = create_engine(db_uri)
    engine.connect()
    print('Hey! You successfully connected to your CockroachDB cluster.')

def main():
    # conn_string = input('Enter your node\'s connection string:\n')
    conn_string = config('CONNECTION_STRING', default='guess_me')

    try:
        db_uri = os.path.expandvars(conn_string)
        db_uri = urllib.parse.unquote(db_uri)
        psycopg_uri = db_uri.replace(
            'postgresql://', 'cockroachdb://').replace(
                'postgres://', 'cockroachdb://')
        connect(psycopg_uri)
    except Exception as e:
        print('Failed to connect to database.')
        print('{0}'.format(e))

if __name__ == '__main__':
    main()