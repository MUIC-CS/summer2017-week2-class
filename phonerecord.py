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
            ret = []
            for row in rs:
                ret.append(PhoneRecord.from_dict(row))
            return ret

if __name__ == '__main__':
    PhoneRecordRepo.create_table()
#####
####
####
####
#####
