import mysql.connector

class DbReading:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'Marsbynight13'

    def connect(self):
        self.connection = mysql.connector.connect(host = self.host,
                                            user = self.user,
                                            password = self.password)

    def get_all_categories(self):
        cursor = self.connection.cursor()
        cursor.execute('USE Purbeurre')

        query = """SELECT * FROM category ORDER BY category.id"""
        
        cursor.execute(query)

        #print(cursor.fetchall())
        return cursor.fetchall()
    
    def display_categories(self, all_categories):
        """Displays the list of categories"""
        for index, categorie in all_categories:
            print(f"{index}. {categorie}")
    


def main():
    test = DbReading()
    test.connect()
    all_categories = test.get_all_categories()
    test.display_categories(all_categories)

if __name__ == "__main__":
    main()