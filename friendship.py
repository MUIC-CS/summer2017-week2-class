from db import get_cursor


class FriendShip:

    def __init__(self, id, left_id, right_id, love):
        self.id = id
        self.left_id = left_id
        self.right_id = right_id
        self.love = love

    @classmethod
    def from_dict(cls, d):
        return FriendShip(d['id'], d['left_id'], d['right_id'], d['love'])


class FriendShipRepo:

    @classmethod
    def create_table(cls):
        with get_cursor() as cur:
            cur.execute(
                """
                DROP TABLE IF EXISTS friendship;
                CREATE TABLE friendship (
                    id SERIAL NOT NULL PRIMARY KEY,
                    left_id INTEGER NOT NULL,
                    right_id INTEGER NOT NULL,
                    love BOOLEAN NOT NULL
                );
                """
            )
            cur.connection.commit()

    @classmethod
    def add_friendship(cls, left, right, love):
        with get_cursor() as cur:
            cur.execute(
                """
                INSERT INTO friendship(left_id, right_id, love)
                VALUES( %s, %s, %s)
                RETURNING id
                """
            )
            cur.connection.commit()
            return cur.fetchone()['id']

    @classmethod
    def find_friend(cls, person, love):
        with get_cursor() as cur:
            cur.execute(
                """
                SELECT *
                FROM friendship
                WHERE (left_id=%s OR right_id=%s) and love=%s
                """,
                (person, person, love)
            )
            return [FriendShip.from_dict(row) for row in cur.fetchall()]
