
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
            LIMIT 15
                """
        cursor.execute(query, (cat_id, prod_id,))
        return cursor.fetchall()

    def one_substitute(self, choiceS):
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
        cursor.execute(query, (choiceS,))
        return cursor.fetchall()

    def add_favorite(self, choiceP, choiceS):
        """Method for adding a product to the favorites table"""
        insert_query = """INSERT INTO Purbeurre.favorite \
                            (id_compared, id_substitute) VALUES (%s, %s)"""
        cursor = self.connect.connection.cursor()
        cursor.execute("""
                        SELECT id_compared, id_substitute \
                        FROM Purbeurre.favorite \
                        WHERE id_compared = %s \
                        AND id_substitute = %s""", (choiceP, choiceS))
        reponse = cursor.fetchone()
        if not reponse:
            cursor.execute(insert_query, (choiceP, choiceS,))
        self.connect.connection.commit()

    def favorite(self):
        """Method for retrieving compared products"""
        cursor = self.connect.connection.cursor()
        cursor.execute('USE Purbeurre')
        query = """
            SELECT
                    compared.id,
                    compared.brands,
                    compared.product_name_fr,
                    compared.nutrition_grade_fr,
                    compared.stores,
                    compared.url,
                    substitute.id,
                    substitute.brands,
                    substitute.product_name_fr,
                    substitute.nutrition_grade_fr,
                    substitute.stores,
                    substitute.url
            FROM
                    Purbeurre.favorite
                    INNER JOIN Purbeurre.products AS compared ON \
                        Purbeurre.favorite.id_compared = compared.id
                    INNER JOIN Purbeurre.products AS substitute ON \
                        Purbeurre.favorite.id_substitute = substitute.id
                """
        cursor.execute(query)
        return cursor.fetchall()
