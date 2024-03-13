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


if __name__ == "__main__":
    CreateUsers()


