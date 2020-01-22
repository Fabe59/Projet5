import mysql.connector


class Connection:
    """Class connection db"""

    def __init__(self):
        """Connection information"""
        self.host = 'localhost'
        self.user = 'root'
        self.password = '13579'

    def connect(self):
        """Connection method"""
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
