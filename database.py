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
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    name VARCHAR(200) NOT NULL UNIQUE,
                    PRIMARY KEY (id))
                    """
        cursor.execute(query_table)
        print("Category table successfully created")

    def create_table_products(self):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        query_table = """
                    CREATE TABLE IF NOT EXISTS `Purbeurre`.`products`(
                    id BIGINT UNSIGNED NOT NULL,
                    brands VARCHAR(100) NOT NULL,
                    product_name_fr VARCHAR(200) NOT NULL,
                    nutrition_grade_fr CHAR(1) NOT NULL,
                    stores VARCHAR(200) NOT NULL,
                    PRIMARY KEY (id));
                    """
        cursor.execute(query_table)
        print("Products table successfully created")

    def create_categories_products(self):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        query_table = """
                    CREATE TABLE IF NOT EXISTS `Purbeurre`.`categories_products`(
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    id_cat INT UNSIGNED NOT NULL,
                    id_prod BIGINT UNSIGNED NOT NULL,
                    CONSTRAINT `fk_id_cat`
                        FOREIGN KEY (`id_cat`) REFERENCES `category`(`id`),
                    CONSTRAINT `fk_id_prod`
                        FOREIGN KEY (`id_prod`) REFERENCES `products`(`id`));
                    """
        cursor.execute(query_table)
        print("Jointure table successfully created")

    def add_categories(self, ordered_cat_list):
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

    def add_products(self, products_list, cat_name):
        insert_query = """
                    INSERT INTO products (id, brands, product_name_fr, nutrition_grade_fr, stores)
                    VALUES (%s, %s, %s, %s, %s)
                    """
        cursor = self.connection.cursor()
        for product in products_list:
            cursor.execute("""SELECT id FROM products WHERE id=%(id)s""", product)
            reponse = cursor.fetchone()
            if not reponse:
                cursor.execute(insert_query, (product['id'], product['brands'], product['product_name_fr'], product['nutrition_grade_fr'], product['stores']))
                self.connection.commit()
                cursor.execute("""SELECT id FROM category WHERE name = %s""", (cat_name,))
                cat_id = cursor.fetchone()
                cursor.execute( """INSERT INTO categories_products (id_cat, id_prod) VALUES (%s, %s)""" , (cat_id[0], product['id']))
        print("Products inserted successfully into Products table")