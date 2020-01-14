from dbreading import DbReading
from database import Database


class Interface:

    def __init__(self):
        self.running = True
        self.dbreading = DbReading()
        self.dbreading.connect()
        self.database = Database()
        self.database.connect()
        self.commands = ['O', 'N', 'Q', 'A']
        self.liste = []


    def menu(self):
        """method who display home menu"""
        print("Bienvenue, que souhaitez faire?\n1 = Substituer un produit \n2 = Revoir les produits déjà substitués \nQ = Quitter")
        choice = input()

        if choice == "1":
            self.categories_menu()
        elif choice == "2":
            print("Voici la liste des produits enregistrés lors de vos dernières recherches:")
            self.dbreading.connect()
            self.dbreading.display_favorite()
            self.menu()
        elif choice == "Q":
            print('À bientôt!')
            self.exit()
        else:
            print("Vous devez entrer le chiffre 1 ou 2 ou tapez Q pour quitter")
            self.menu()
    
    def categories_menu(self):
        """method who display all categories"""
        all_categories = self.dbreading.get_all_categories()
        for number, name in all_categories:
            self.liste.append(number)
        self.dbreading.display_categories(all_categories)
        choiceC = self.input_user('\nChoisisez une catégorie: ')

        if choiceC == "A":
            self.menu()
        elif choiceC == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.products_menu(choiceC)

    def products_menu(self, choiceC):
        """method who display all products of a catagory"""
        print("Voici la liste des produits présents dans la catégorie choisie:")
        all_products = self.dbreading.get_products_category(choiceC)
        for number, brand, name, nutriscore, stores, url in all_products:
            self.liste.append(number)
        self.dbreading.display_products(all_products)
        choiceP = self.input_user("Choisissez un produit parmi la liste en indiquant son numéro de produit: ")

        if choiceP == "A":
            self.menu()
        elif choiceP == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.get_all_substitute(choiceC, choiceP)

    def get_all_substitute(self, choiceC, choiceP):
        """method who display all subsitutes"""
        print("Voici la liste des produits dont le nutriscore est meilleur que celui du produit initial:")
        all_substitute = self.dbreading.get_all_substitute(choiceC, choiceP)
        for number, brand, name, nutriscore, stores, url in all_substitute:
            self.liste.append(number)
        self.dbreading.display_all_substitute(all_substitute)
        choiceS = self.input_user("\nChoisissez un substitut parmi la liste en indiquant son numéro de produit: ")

        if choiceS == "A":
            self.menu()
        elif choiceS == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.one_substitute(choiceS)

    def one_substitute(self, choiceS):
        """Method who display the substitute choice and ask to the user if he/she wants to save it"""
        print("Vous avez choisi :")
        one_substitute = self.dbreading.one_substitute(choiceS)
        self.dbreading.display_one_substitute(one_substitute)
        save = input('\nSouhaitez vous en enregistrer ce produit? (O pour Oui, N pour Non)')

        if save == "A":
            self.menu()
        elif save == "N":
            print("A bientôt!")
            self.exit()
        elif save == "O":
            self.database.add_favorite(choiceS)
            print("produit sauvegardé\n")
            self.menu()
    
    def input_user(self, message):
        """User input recovery method"""
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

                except:
                    print("Choix incorrect \n")

        return user

    def exit(self):
        """Method to get out of the loop"""
        self.running = False


def main():
    test = Interface()
    test.menu()


if __name__ == "__main__":
    main()