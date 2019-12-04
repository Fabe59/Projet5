import mysql.connector

class MySQL:
     
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'XXX'

    def connect(self):
        self.connection = mysql.connector.connect(host = self.host,
                                            user = self.user,
                                            password = self.password)
        if self.connection.is_connected():
            db_Info = self.connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)

    def create_db(self):
        cursor = self.connection.cursor()
        query_db = """
                CREATE DATABASE IF NOT EXISTS Purbeurre CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
                """
        cursor.execute(query_db)

    def create_table_category(self):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        query_table = """
                    CREATE TABLE IF NOT EXISTS `Purbeurre`.`category`(
                    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    name VARCHAR(200) NOT NULL UNIQUE,
                    PRIMARY KEY (id));
                    """
        cursor.execute(query_table)

