import mysql.connector

class Connection:
     
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'XXX'

    def connect(self):
        self.connection = mysql.connector.connect(host = self.host,
                                            user = self.user,
                                            password = self.password)
        if self.connection.is_connected():
            db_Info = self.connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
    