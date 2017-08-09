from db import get_cursor


class FriendShip:

    def __init__(self, id, left, right, love):
        self.id = id
        self.left = left
        self.right = right
        self.love = love


class FriendShipRepo:

    @classmethod
    def create_table(cls):
        with get_cursor() as cur:
            cur.execute(
                """
                DROP IF EXISTS friendship;
                CREATE TABLE friendship (
                    id SERIAL NOT NULL PRIMARY KEY,
                    left INTEGER NOT NULL,
                    right INTEGER NOT NULL,
                    love BOOLEAN NOT NULL
                );
                """
            )
            cur.connection.commit()

    def add_friendship(cls, left, right, love):

        #
        #
        #
        #
        #
        #
        #
        #
        #
