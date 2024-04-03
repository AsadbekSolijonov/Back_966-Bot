import logging
import sqlite3


class DBConnection:
    """
    Database connection
    """

    def __init__(self):
        """
        build constructor
        """
        self.conn = sqlite3.connect('/Users/asadbeksolijonov/MarsPY/Back_966/oy_4/bot_project/utils/db_api/datas.db')
        self.curr = self.conn.cursor()
        # Create Table
        self.create_table()

    def create_table(self):
        """For auto create table"""
        pass


class CreateUsers(DBConnection):
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users(
        chat_id INT NOT NULL ,
        username TEXT,
        phone INT,
        address varchar(50),
        language TEXT,
        PRIMARY KEY (chat_id));
        """
        with self.conn:
            self.curr.execute(query)


class UsersFunctionality(CreateUsers):
    def insert_into(self, chat_id):
        """Ma'lumot qo'shish uchun.
        chat_id: int - foydalunvchini telegram chat_id si
        username: str - foydalunvchini telegram username mi
        phone: int - foydalunuvchini telegram telefon nomeri
        address: str - foydalunuvchini yashash manzili
        """

        query = f"""
        INSERT INTO users (chat_id) VALUES ({chat_id});
        """
        with self.conn:
            self.curr.execute(query)

    def update_user(self, chat_id, username, phone, address):
        query = f"""
        UPDATE users SET username = '{username}', phone={phone}, address='{address}' WHERE chat_id={chat_id};"""

        with self.conn:
            self.curr.execute(query)
        logging.info(f'Foydalanuvchi <{chat_id}> ma`lumoti yangilandi!')

    def update_language(self, chat_id, language):
        query = f"""
        UPDATE users  SET language='{language}' WHERE chat_id={chat_id};
        """
        with self.conn:
            self.curr.execute(query)
        logging.info(f'Foydalanuvchi <{chat_id}> ma`lumoti yangilandi!')

    def get_all(self, chat_id):
        query = f"""
        SELECT * FROM users WHERE chat_id={chat_id}
        """

        datas = self.curr.execute(query).fetchone()
        return [] if not datas else datas

    def get_followers_count(self):
        query = """SELECT count(*) FROM users"""
        followers = self.curr.execute(query).fetchone()[0]
        return followers

    def get_followers(self):
        query = """
        SELECT * FROM users;"""
        datas = self.curr.execute(query).fetchall()
        return datas

    def del_user(self, chat_id):
        query = f"""
        DELETE FROM users WHERE chat_id={chat_id}"""
        with self.conn:
            self.curr.execute(query)

    def get_language(self, chat_id):
        query = f"""
        SELECT language FROM users WHERE chat_id={chat_id}"""
        data = self.curr.execute(query).fetchone()

        return data[0] if data else 'uz'


if __name__ == "__main__":
    CreateUsers()
