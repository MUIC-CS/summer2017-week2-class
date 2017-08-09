from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import DictCursor
from contextlib import contextmanager
import os

env = os.getenv('TABKEEPER_ENV', 'development')

setting = {
    'dbname': 'hello',
    'user': 'postgres',
    'host': 'localhost',
    'password': ''
}


pool = ThreadedConnectionPool(1, 20,
                              dbname=setting['dbname'],
                              user=setting['user'],
                              host=setting['host'],
                              password=setting['password'])


@contextmanager
def get_cursor():
    con = pool.getconn()
    try:
        yield con.cursor(cursor_factory=DictCursor)
    finally:
        pool.putconn(con)
