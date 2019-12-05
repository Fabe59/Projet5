from database import Database

class App:

    def run(self):
        mysql = Database()
        mysql.connect()
        mysql.create_db()
        mysql.create_table_category()
        mysql.create_table_products()
        mysql.test()

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
