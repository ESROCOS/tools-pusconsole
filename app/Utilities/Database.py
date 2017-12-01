import sqlite3 as sq3
from sqlite3 import Error


class Database(object):

    def __init__(self, dbname: str):
        self.db = None
        self.cursor = None
        self.open_db(dbname)
        self.create_table()

    def create_table(self, table_name: str = "packages"):
        query = """CREATE TABLE
                    IF NOT EXISTS """ + table_name + """(
                        type text,
                        serv_id integer,
                        msg_id integer,
                        time text,
                        src integer,
                        des integer,
                        seq integer,
                        status text,
                        info text,
                        rest_of_data json
                    );"""

        self.cursor.execute(query)

    def open_db(self, db_name: str):
        try:
            self.db = sq3.connect(db_name)
            self.cursor = self.db.cursor()
        except Error as e:
            print(e)

    def query_db(self, query: str, _list: tuple = None):
        """
        This methods execute a query or an insertion in the db
        :param query: Query using prepared statement
        :param _list: Parameters of the prepared statement
        :return: Results of the query
        """
        if _list is None:
            return self.cursor.execute(query)
        else:
            return self.cursor.execute(query, _list)

    def insert_db(self, query: str, _list: list = None):
        """
        This methods execute an insertion in the db
        :param query: Query using prepared statement
        :param _list: Parameters of the prepared statement
        """
        self.cursor.executemany(query, _list)
        self.db.commit()
