from db import get_cursor


class PhoneRecord:

    def __init__(self, id, name, phoneno):
        self.id = id
        self.name = name
        self.phoneno = phoneno


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

if __name__ == '__main__':
    PhoneRecordRepo.create_table()
#####
####
####
####
#####
