from database import Database
from categoryFromApi import CategoryFromApi
from productFromApi import ProductFromApi
from interface import Interface


class App:

    def run(self):
        mysql = Database()
        mysql.connect()
        mysql.create_db()
        mysql.create_table_category()
        mysql.create_table_products()
        mysql.create_categories_products()
        categories = CategoryFromApi()
        categories_bd = mysql.add_categories(categories.get_categories())
        products = ProductFromApi()
        for cat in categories_bd:
            mysql.add_products(products.get_products(cat[1]), cat[0])
        itf = Interface()
        itf.menu()




def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
