import mysql.connector

class DbReading:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '**********'

    def connect(self):
        self.connection = mysql.connector.connect(host = self.host,
                                            user = self.user,
                                            password = self.password)

    def get_all_categories(self):
        cursor = self.connection.cursor()
        cursor.execute('USE Purbeurre')

        query = """SELECT * FROM category ORDER BY category.id"""
        
        cursor.execute(query)
        return cursor.fetchall()
    
    def display_categories(self, all_categories):
        """Displays the list of categories"""
        for index, categorie in all_categories:
            print(f"{index}. {categorie}")

    def get_products_category(self, cat_id):
        cursor = self.connection.cursor()
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
	            Purbeurre.category, Purbeurre.products, Purbeurre.categories_products
            WHERE
	            Purbeurre.category.id = Purbeurre.categories_products.id_cat
                AND
                Purbeurre.products.id = Purbeurre.categories_products.id_prod
                AND
                Purbeurre.categories_products.id_cat = %s
            ORDER BY Purbeurre.products.product_name_fr
                """
        
        cursor.execute(query, (cat_id,))
        return cursor.fetchall()
     
    def display_products(self, all_products):
        """Show product list"""
        for prod_id, brand, name, nutriscore, stores, url in all_products:
            print(f"\n{prod_id}\n MARQUE: {brand.upper()}\n PRODUIT: {name}\n NUTRISCORE: {nutriscore.upper()}\n POINTS DE VENTE: {stores}\n URL: {url}\n")

    def get_all_substitute(self, cat_id, prod_id):
        cursor = self.connection.cursor()
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
	            Purbeurre.category, Purbeurre.products, Purbeurre.categories_products
            WHERE
	            Purbeurre.category.id = Purbeurre.categories_products.id_cat
	            AND
	            Purbeurre.products.id = Purbeurre.categories_products.id_prod
	            AND
	            Purbeurre.categories_products.id_cat= %s
                AND
                Purbeurre.products.nutrition_grade_fr < (SELECT products.nutrition_grade_fr FROM Purbeurre.products WHERE id = %s)
            ORDER BY Purbeurre.products.nutrition_grade_fr
            LIMIT 10
                """
        cursor.execute(query, (cat_id, prod_id,))
        return cursor.fetchall()

    def display_all_substitute(self, all_substitute):
        """Show product list"""
        for prod_id, brand, name, nutriscore, stores, url in all_substitute:
            print(f"\n{prod_id}\n MARQUE: {brand.upper()}\n PRODUIT: {name}\n NUTRISCORE: {nutriscore.upper()}\n POINTS DE VENTE: {stores}\n URL: {url}")
    
    def one_substitute(self, choiseS):
        cursor = self.connection.cursor()
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
	            Purbeurre.category, Purbeurre.products, Purbeurre.categories_products
            WHERE
	            Purbeurre.category.id = Purbeurre.categories_products.id_cat
                AND
                Purbeurre.products.id = Purbeurre.categories_products.id_prod
                AND
                Purbeurre.categories_products.id_prod = %s
                """
        cursor.execute(query, (choiseS,))
        return cursor.fetchall()
        #print(one)

    def display_one_substitute(self, one_substitute):
        """Show substitute selected"""
        for prod_id, brand, name, nutriscore, stores, url in one_substitute:
            print(f"\n{prod_id}\n MARQUE: {brand.upper()}\n PRODUIT: {name}\n NUTRISCORE: {nutriscore.upper()}\n POINTS DE VENTE: {stores}\n URL: {url}")

    def add_favorite(self, choiceS):
        insert_query = """INSERT INTO Purbeurre.favorite (id_result) VALUES (%s)"""
        cursor = self.connection.cursor()
        cursor.execute(insert_query, (choiceS,))
        self.connection.commit()

    def display_favorite(self):
        cursor = self.connection.cursor()
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
	            Purbeurre.products.id = Purbeurre.favorite.id_result
            """
        cursor.execute(query)
        fav = cursor.fetchall()
        #print(reponse)
        for prod_id, brand, name, nutriscore, stores, url in fav:
            print(f"\n{prod_id}\n MARQUE: {brand.upper()}\n PRODUIT: {name}\n NUTRISCORE: {nutriscore.upper()}\n POINTS DE VENTE: {stores}\n URL: {url}\n")
