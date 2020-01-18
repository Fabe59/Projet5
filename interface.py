from connection import Connection
from dbuser import DbUser
from dbadmin import DbAdmin


class Interface:

    def __init__(self, auth):
        self.running = True
        self.dbuser = DbUser(auth)
        self.dbadmin = DbAdmin(auth)
        self.commands = ['O', 'N', 'Q', 'A']
        self.liste = []
        self.cat_number = []

    def menu(self):
        """method who display home menu"""
        print("Bienvenue, que souhaitez vous faire?\n1 = Substituer un produit \
            \n2 = Revoir les produits déjà substitués \nQ = Quitter")
        choice = input()

        if choice == "1":
            self.categories_menu()
        elif choice == "2":
            print("Voici la liste des produits enregistrés "
                  "lors de vos dernières recherches:")
            fav = self.dbuser.favorite()
            for idC, brandC, nameC, nutriC, storesC, urlC, \
                    idS, brandS, nameS, nutriS, storesS, urlS in fav:
                print(f"""Vous aviez choisi de substituer:
                {idC}
                MARQUE : {brandC.upper()}
                PRODUIT: {nameC}
                NUTRISCORE: {nutriC.upper()}
                POINTS DE VENTE: {storesC}
                URL: {urlC}""")
                print(f"""par:
                {idS}
                MARQUE : {brandS.upper()}
                PRODUIT: {nameS}
                NUTRISCORE: {nutriS.upper()}
                POINTS DE VENTE: {storesS}
                URL: {urlS}\n""")
            self.menu()
        elif choice == "Q":
            print('À bientôt!')
            self.exit()
        else:
            print("Vous devez entrer le chiffre 1 ou 2 "
                  "ou tapez Q pour quitter")
            self.menu()

    def categories_menu(self):
        """method who display all categories"""
        all_categories = self.dbuser.get_all_categories()
        for index, categorie in all_categories:
            self.cat_number.append(index)
            print(f"{index}. {categorie}")
        choiceC = self.inputC_user(
                    "Choisisez une catégorie en indiquant son numéro, "
                    "'A' pour revenir au menu principal, "
                    "'Q' pour Quitter : ")

        if choiceC == "A":
            self.menu()
        elif choiceC == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.products_menu(choiceC)

    def products_menu(self, choiceC):
        """method who display all products of a catagory"""
        print("Voici la liste des produits présents dans la catégorie:")
        all_products = self.dbuser.get_products_category(choiceC)
        for prod_id, brand, name, nutriscore, stores, url in all_products:
            self.liste.append(prod_id)
            print(f"""
            {prod_id}
            MARQUE: {brand.upper()}
            PRODUIT: {name}
            NUTRISCORE: {nutriscore.upper()}
            POINTS DE VENTE: {stores}
            URL: {url}\n""")
        choiceP = self.input_user(
            "Choisissez un produit parmi la liste en indiquant, "
            "son numéro de produit, "
            "'A' pour revenir au menu des categories, "
            "'Q' pour Quitter : ")

        if choiceP == "A":
            self.categories_menu()
        elif choiceP == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.get_all_substitute(choiceC, choiceP)

    def get_all_substitute(self, choiceC, choiceP):
        """method who display all subsitutes"""
        print(
            "Voici la liste des produits dont le nutriscore est meilleur "
            "que celui du produit initial:")
        all_substitute = self.dbuser.get_all_substitute(choiceC, choiceP)
        for prod_id, brand, name, nutriscore, stores, url in all_substitute:
            self.liste.append(prod_id)
            print(f"""
            {prod_id}
            MARQUE: {brand.upper()}
            PRODUIT: {name}
            NUTRISCORE: {nutriscore.upper()}
            POINTS DE VENTE: {stores}
            URL: {url}\n""")
        choiceS = self.input_user(
            "Choisissez un substitut parmi la liste en indiquant "
            "son numéro de produit, 'A' pour revenir au menu principal, "
            "'Q' pour Quitter : ")

        if choiceS == "A":
            self.menu()
        elif choiceS == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.one_substitute(choiceP, choiceS)

    def one_substitute(self, choiceP, choiceS):
        """Method who display the substitute choice \
            and ask to the user if he/she wants to save it"""
        print("Vous avez choisi :")
        one_substitute = self.dbuser.one_substitute(choiceS)
        for prod_id, brand, name, nutriscore, stores, url in one_substitute:
            print(f"""
            {prod_id}
            MARQUE: {brand.upper()}
            PRODUIT: {name}
            NUTRISCORE: {nutriscore.upper()}
            POINTS DE VENTE: {stores}
            URL: {url}\n""")
        save = input(
            "Souhaitez vous en enregistrer ce produit "
            "(O = Oui, N = Non)?")

        if save == "A":
            self.menu()
        elif save == "N":
            print("A bientôt!")
            self.exit()
        elif save == "O":
            self.dbuser.add_favorite(choiceP, choiceS)
            print("produit sauvegardé\n")
            self.menu()

    def inputC_user(self, message):
        """Method for retrieving and checking \
            the category chosen by the user"""
        while True:
            user = input(message)

            if user in self.commands:
                return user

            else:
                try:
                    user = int(user)
                    assert user in self.cat_number
                    break

                except Exception:
                    print("CHOIX DE CATEGORIE INCORRECT \n")

        return user

    def input_user(self, message):
        """Method for retrieving and checking the product \
            and substitute chosen by the user"""
        while True:
            user = input(message)

            if user in self.commands:
                return user

            else:
                try:
                    user = int(user)
                    assert user >= 1
                    assert user in self.liste
                    break

                except Exception:
                    print("CHOIX INCORRECT \n")

        return user

    def exit(self):
        """Method to get out of the loop"""
        self.running = False


def main():
    auth = Connection()
    auth.connect()
    interface = Interface(auth)
    interface.menu()


if __name__ == "__main__":
    main()
