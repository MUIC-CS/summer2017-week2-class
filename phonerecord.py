from db import get_cursor


class PhoneRecord:

    def __init__(self, id, name, phoneno):
        self.id = id
        self.name = name
        self.phoneno = phoneno

    @classmethod
    def from_dict(cls, d):
        return PhoneRecord(d['id'], d['name'], d['phoneno'])

    def __repr__(self):
        return "<PhoneRecord id={id} name={name} phoneno={phoneno}>".format(
            id=self.id,
            name=self.name,
            phoneno=self.phoneno
        )


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
    def find_by_id(cls, id):
        with get_cursor() as cur:
            cur.execute(
                """
                SELECT * FROM phonerecords WHERE id=%s
                """,
                (id,)
            )
            rs = cur.fetchone()
            return PhoneRecord.from_dict(rs)

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

    @classmethod
    def delete_by_id(cls, id):
        with get_cursor() as cur:
            cur.execute(
                """
                DELETE FROM phonerecords WHERE id=%s
                """,
                (id, )
            )
            cur.connection.commit()


if __name__ == '__main__':
    PhoneRecordRepo.create_table()

    kfc = PhoneRecord(None, 'KFC', '1150')
    mcdonald = PhoneRecord(None, 'McDonald', '1711')
    pizza = PhoneRecord(None, 'Pizza Company', '1112')
    chester = PhoneRecord(None, 'Chester Grill', '1145')

    PhoneRecordRepo.add(kfc)
    PhoneRecordRepo.add(mcdonald)
    PhoneRecordRepo.add(pizza)
    PhoneRecordRepo.add(chester)

    all = PhoneRecordRepo.find_all()
    print all


#####
####
####
####
#####
