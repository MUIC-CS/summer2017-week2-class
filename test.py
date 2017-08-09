import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    host='localhost',
    dbname='hello',
    user='postgres',
    password='')

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
name = 'hello); DROP TABLE example; SELECT 1 + (2'

cursor.execute(
    """
    INSERT INTO example(name) VALUES(%s)
    """,
    (name, )
)

cursor.connection.commit()

cursor.execute(
    """
    SELECT * FROM example
    """
)
rs = cursor.fetchall()
for row in rs:
    print row['name']


#########
