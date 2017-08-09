from db import get_cursor


class PhoneRecord:

    def __init__(self, id, name, phoneno):
        self.id = id
        self.name = name
        self.phoneno = phoneno

    @classmethod
    def from_dict(cls, d):
        return PhoneRecord(d['id'], d['name'], d['phoneno'])


class PhoneRecordRepo:

    @classmethod  # static method
    def create_table(cls):
        with get_cursor() as cur:
            cur.execute(
                """
                DROP TABLE IF EXISTS phonerecords;
                CREATE TABLE phonerecords (
                    id SERIAL NOT NULL PRIMARY KEY,
                    name TEXT NOT NULL,
                    phoneno TEXT NOT NULL
                );
                """
            )
            cur.connection.commit()

    @classmethod
    def find_all(cls):
        with get_cursor() as cur:
            cur.execute(
                """
                SELECT * FROM phonerecords
                """
            )
            rs = cur.fetchall()
            return [PhoneRecord.from_dict(row) for row in rs]

    @classmethod
    def add(cls, obj):
        with get_cursor() as cur:
            cur.execute(
                """
                INSERT INTO phonerecords(name, phoneno)
                VALUES(%s, %s)
                RETURNING id
                """,
                (obj.name, obj.phoneno)
            )
            rs = cur.fetchone()
            obj.id = rs['id']
            cur.connection.commit()
            return obj


if __name__ == '__main__':
    PhoneRecordRepo.create_table()
#####
####
####
####
#####
