from connection import Connection
from dbwriting import Database
from categoryFromApi import CategoryFromApi
from productFromApi import ProductFromApi


class DbInstall:

    def run(self):
        auth = Connection()
        auth.connect()
        mysql = Database(auth)
        mysql.create_db()
        mysql.create_table_category()
        mysql.create_table_products()
        mysql.create_categories_products()
        mysql.create_favorite_table()
        categories = CategoryFromApi()
        categories_bd = mysql.add_categories(categories.get_categories())
        products = ProductFromApi()
        for cat in categories_bd:
            mysql.add_products(products.get_products(cat[1]), cat[0])


def main():
    db = DbInstall()
    db.run()

if __name__ == "__main__":
    main()
