
class DbUser:

    def __init__(self, connection):
        """Connection initialization"""
        self.connect = connection

    def get_all_categories(self):
        """Category retrieval method"""
        cursor = self.connect.connection.cursor()
        cursor.execute('USE Purbeurre')

        query = """SELECT * FROM category ORDER BY category.id"""

        cursor.execute(query)
        return cursor.fetchall()

    def get_products_category(self, cat_id):
        """Method for retrieving products from a category"""
        cursor = self.connect.connection.cursor()
        cursor.execute('USE Purbeurre')
        query = """
            SELECT
                    products.id,
                    products.brands,
                    products.product_name_fr,
                    products.nutrition_grade_fr,
                    products.stores,
                    products.url
            FROM
                    Purbeurre.category, Purbeurre.products,
                        Purbeurre.categories_products
            WHERE
                    Purbeurre.category.id =
                        Purbeurre.categories_products.id_cat
                    AND
                    Purbeurre.products.id =
                        Purbeurre.categories_products.id_prod
                    AND
                    Purbeurre.categories_products.id_cat = %s
            ORDER BY Purbeurre.products.product_name_fr
                """

        cursor.execute(query, (cat_id,))
        return cursor.fetchall()

    def get_all_substitute(self, cat_id, prod_id):
        """Method for obtaining substitutes for a product"""
        cursor = self.connect.connection.cursor()
        cursor.execute('USE Purbeurre')
        query = """
            SELECT
                    products.id,
                    products.brands,
                    products.product_name_fr,
                    products.nutrition_grade_fr,
                    products.stores,
                    products.url
            FROM
                    Purbeurre.category, Purbeurre.products, \
                        Purbeurre.categories_products
            WHERE
                    Purbeurre.category.id = \
                        Purbeurre.categories_products.id_cat
                    AND
                    Purbeurre.products.id = \
                        Purbeurre.categories_products.id_prod
                    AND
                    Purbeurre.categories_products.id_cat= %s
                    AND
                    Purbeurre.products.nutrition_grade_fr < \
                        (SELECT products.nutrition_grade_fr FROM \
                            Purbeurre.products WHERE id = %s)
            ORDER BY Purbeurre.products.product_name_fr
            LIMIT 10
                """
        cursor.execute(query, (cat_id, prod_id,))
        return cursor.fetchall()

    def one_substitute(self, choiseS):
        """Method to retrieve only the info of the selected product"""
        cursor = self.connect.connection.cursor()
        cursor.execute('USE Purbeurre')
        query = """
            SELECT
                    products.id,
                    products.brands,
                    products.product_name_fr,
                    products.nutrition_grade_fr,
                    products.stores,
                    products.url
            FROM
                    Purbeurre.products
            WHERE
                    Purbeurre.products.id = %s
                """
        cursor.execute(query, (choiseS,))
        return cursor.fetchall()

    def add_favorite(self, choiceS):
        """Method for adding a product to the favorites table"""
        insert_query = """INSERT INTO Purbeurre.favorite (id_substitute) \
                            VALUES (%s)"""
        cursor = self.connect.connection.cursor()
        cursor.execute(insert_query, (choiceS,))
        self.connect.connection.commit()

    def favorite(self):
        """Method for retrieving favorite table products"""
        cursor = self.connect.connection.cursor()
        cursor.execute('USE Purbeurre')
        query = """
            SELECT
                products.id,
                products.brands,
                products.product_name_fr,
                products.nutrition_grade_fr,
                products.stores,
                products.url
            FROM
                Purbeurre.products, Purbeurre.favorite
            WHERE
                Purbeurre.products.id = Purbeurre.favorite.id_substitute
                """
        cursor.execute(query)
        return cursor.fetchall()
