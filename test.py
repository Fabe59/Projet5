from connection import Connection
from dbuser import DbUser
from dbinstall import DbInstall


class Test:

    def __init__(self):
        pass


def main():
    db = DbInstall()
    db.run()
    auth = Connection()
    auth.connect()
    testdbuser = DbUser(auth)
    testdbuser.get_all_categories()
    testdbuser.get_products_category(1)
    testdbuser.get_all_substitute(1, 3229820160672)
    testdbuser.one_substitute(3229820782560)
    testdbuser.add_favorite(3229820160672, 3229820782560)
    testdbuser.favorite()


if __name__ == "__main__":
    main()
