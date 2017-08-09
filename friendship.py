from db import get_cursor


class FriendShip:

    def __init__(self, id, left, right, love):
        self.id = id
        self.left = left
        self.right = right
        self.love = love

    @classmethod
    def from_dict(cls, d):
        return FriendShip(d['id'], d['left'], d['right'], d['love'])


class FriendShipRepo:

    @classmethod
    def create_table(cls):
        with get_cursor() as cur:
            cur.execute(
                """
                DROP TABLE IF EXISTS friendship;
                CREATE TABLE friendship (
                    id SERIAL NOT NULL PRIMARY KEY,
                    left INTEGER NOT NULL,
                    right INTEGER NOT NULL,
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
                INSERT INTO friendship(left, right, love)
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
                WHERE (left=%s OR right=%s) and love=%s
                """,
                (person, person, love)
            )
            return [FriendShip.from_dict(row) for row in cur.fetchall()]
