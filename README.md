This repo contains the source code for a simple Hello World application, written in Python. The app uses the [SQLAlchemy ORM framework](https://docs.sqlalchemy.org/en/latest/) to connect to an existing CockroachDB cluster.

To run the code:

1. Start a [local CockroachDB cluster](https://www.cockroachlabs.com/docs/stable/secure-a-cluster.html), or use [CockroachCloud](https://www.cockroachlabs.com/docs/cockroachcloud/create-a-free-cluster.html).
2. From the command line, execute the following:

    ~~~
    virtualenv env
    ~~~
    ~~~
    source env/bin/activate
    ~~~
    ~~~
    pip3 install sqlalchemy sqlalchemy-cockroachdb psycopg2 python-decouple
    ~~~
    ~~~
    python3 main.py
    ~~~
    ~~~
    deactivate
    ~~~

3. Enter the connection string for the cluster.

    **Note:** The connection string must begin with the prefix `cockroachdb` and must specify the database to which to connect.

    For example, for a local, demo cluster:
    `cockroachdb://demo:<demo_password>@127.0.0.1:26257/defaultdb?sslmode=require`

    For CockroachCloud:
    `cockroachdb://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>`
