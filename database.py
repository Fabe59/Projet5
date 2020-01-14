import mysql.connector

class Database:
     
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '**********'

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
                    url VARCHAR(500) NOT NULL,
                    PRIMARY KEY (id));
                    """
        cursor.execute(query_table)
        print("Products table successfully created")

    def create_categories_products(self):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        query_table = """
                    CREATE TABLE IF NOT EXISTS `Purbeurre`.`categories_products`(
                    id_cat INT UNSIGNED NOT NULL,
                    id_prod BIGINT UNSIGNED NOT NULL,
                    PRIMARY KEY (id_cat, id_prod),
                    CONSTRAINT `fk_id_cat`
                        FOREIGN KEY (`id_cat`) REFERENCES `category`(`id`),
                    CONSTRAINT `fk_id_prod`
                        FOREIGN KEY (`id_prod`) REFERENCES `products`(`id`));
                    """
        cursor.execute(query_table)
        print("Jointure table successfully created")

    def create_favorite_table(self):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        query_table = """
                    CREATE TABLE IF NOT EXISTS `Purbeurre`.`favorite` (
                    id_result BIGINT UNSIGNED NOT NULL,
                    PRIMARY KEY (id_result));
                    """
        cursor.execute(query_table)
        print("Favorite table successfully created")

    def add_categories(self, ordered_cat_list):
        cursor = self.connection.cursor()
        cursor.execute("USE `Purbeurre`")
        insert_query = """
                    INSERT INTO category (name) 
                    VALUES (%s)
                    """
        ids = []
        for category in ordered_cat_list:
            cursor.execute(insert_query, (category,))
            id = (cursor.lastrowid, category)
            ids.append(id)
        self.connection.commit()
        return ids

    def add_products(self, products_list, cat_id):
        insert_query = """
                    INSERT INTO products (id, brands, product_name_fr, nutrition_grade_fr, stores, url)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
        cursor = self.connection.cursor()
        for product in products_list:
            cursor.execute("""SELECT id FROM products WHERE id=%(id)s""", product)
            reponse = cursor.fetchone()
            if not reponse:
                cursor.execute(insert_query, (product['id'], product['brands'], product['product_name_fr'], product['nutrition_grade_fr'], product['stores'], product['url']))
                self.connection.commit()
            cursor.execute("""INSERT INTO categories_products (id_cat, id_prod) VALUES (%s, %s)""" , (cat_id, product['id']))
            self.connection.commit()
        print("Products inserted successfully into Products table")

    def add_favorite(self, choiceS):
        insert_query = """INSERT INTO Purbeurre.favorite (id_result) VALUES (%s)"""
        cursor = self.connection.cursor()
        cursor.execute(insert_query, (choiceS,))
        self.connection.commit()
        
