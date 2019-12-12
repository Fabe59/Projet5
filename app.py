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
        name_categories = category.get_category()
        mysql.add_category(name_categories)
        products = ProductFromApi()
        all_products = {}
        for name_category in name_categories:
            all_products['name_categories'] = products.get_product(name_category)



def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
