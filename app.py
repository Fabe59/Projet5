from database import Database
from categoryFromApi import CategoryFromApi
from productFromApi import ProductFromApi


class App:

    def run(self):
        mysql = Database()
        mysql.connect()
        mysql.create_db()
        mysql.create_table_category()
        mysql.create_table_products()
        mysql.create_categories_products()
        categories = CategoryFromApi()
        categories_id = mysql.add_categories(categories.get_categories())
        products = ProductFromApi()
        for name_category in categories.get_categories():
            mysql.add_products(products.get_products(name_category), categories_id)




def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
