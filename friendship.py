from db import get_cursor


class FriendShip:

    def __init__(self, id, left, right, level):
        self.id = id
        self.left = left
        self.right = right
        self.level = level


class FriendShipRepo:

    @classmethod
    def create_table(cls):
        with get_cursor() as cur:
            cur.execute(
                """
                DROP IF EXISTS friendship;
                CREATE TABLE friendship (
                    id SERIAL NOT NULL PRIMARY KEY,
                    left integer NOT NULL,
                    right integer NOT NULL,
                    level VARCHAR(255) NOT NULL
                );
                """
            )
            cur.connection.commit()
#
#
#
#
#
#
#
#
#
