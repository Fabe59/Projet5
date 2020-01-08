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
        for cat_id, categorie in all_categories:
            print(f"{cat_id}. {categorie}")

    def get_products_category(self, cat_id):
        cursor = self.connection.cursor()
        cursor.execute('USE Purbeurre')
        query = """
            SELECT 
	            products.brands,
	            products.product_name_fr,
	            products.nutrition_grade_fr,
	            products.stores
            FROM 
	            Purbeurre.category, Purbeurre.products, Purbeurre.categories_products
            WHERE
	            Purbeurre.category.id = Purbeurre.categories_products.id_cat
                AND
                Purbeurre.products.id = Purbeurre.categories_products.id_prod
                AND
                Purbeurre.categories_products.id_cat = %s
                """
        
        cursor.execute(query, (cat_id,))
        return cursor.fetchall()
     

    def display_products(self, all_products):
        """Show product list"""
        for id, product in enumerate(all_products):
            print(f"{id+1}. {product}")
    


def main():
    test = DbReading()
    test.connect()
    #all_categories = test.get_all_categories()
    #test.display_categories(all_categories)
    choice = test.get_products_category(1)
    test.display_products(choice)

if __name__ == "__main__":
    main()