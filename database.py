import mysql.connector

class Database:
     
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'XXXXXXXXXX'

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
        print("Database successfully created")

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
        print("Category table successfully created")

    def create_table_products(self):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        query_table = """
                    CREATE TABLE IF NOT EXISTS `Purbeurre`.`products`(
                    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    brand VARCHAR(100) NOT NULL,
                    name VARCHAR(200) NOT NULL UNIQUE,
                    nutriscore CHAR(1) NOT NULL,
                    store VARCHAR(200) NOT NULL,
                    PRIMARY KEY (id));
                    """
        cursor.execute(query_table)
        print("Products table successfully created")

    def add_category(self, ordered_cat_list):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        insert_query = """
                    INSERT INTO category (name) 
                    VALUES (%s)
                    """
        for category in ordered_cat_list:
            cursor.execute(insert_query, (category,))
            self.connection.commit()
        print("Category inserted successfully into Category table")

    def add_product(self, product_list):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        insert_query = """
                    INSERT INTO product (brand, product_name_fr, nutrition_grade_fr, store) 
                    VALUES (%s, %s, %s, %s)
                    """
        
        for product in product_list:
            cursor.execute(insert_query, (brand, product_name_fr, nutrition_grade_fr, store))
            self.connection.commit()
        print("Products inserted successfully into Products table")


    
