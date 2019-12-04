from mysql_connect import Connection

class App:

    def run(self):
        mysql = Connection()
        mysql.connect()
        mysql.create_db()
        mysql.create_table_category()

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
