from sqlalchemy import create_engine
import urllib
import os


def connect(db_uri):
    engine = create_engine(db_uri)
    engine.connect()
    print('Hey! You successfully connected to your CockroachDB cluster.')


if __name__ == '__main__':
    conn_string = input('Enter your node\'s connection string:\n')
    # For cockroach demo:
    # cockroachdb://demo:<demo_password>@127.0.0.1:26257/defaultdb?sslmode=require
    # For CockroachCloud:
    # cockroachdb://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>

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
