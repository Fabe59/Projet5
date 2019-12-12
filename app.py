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
        category = CategoryFromApi()
        name_cat = category.get_category()
        mysql.add_category(name_cat)
        products = ProductFromApi()
        all_products = products.get_product(name_cat)



def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
