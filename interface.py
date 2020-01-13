from dbreading import DbReading
from database import Database


class Interface:

    def __init__(self):
        self.running = True
        self.dbreading = DbReading()
        self.dbreading.connect()
        self.database = Database()
        self.database.connect()


    def menu(self):
        """method who display home menu"""
        print("Bienvenue, que souhaitez faire?\n1 = Substituer un produit \n2 = Revoir les produits déjà substitués \nQ = Quitter")
        choice = input()

        if choice == "1":
            self.categories_menu()
        elif choice == "2":
            print("Vous avez choisi de revoir vos produits subsitués")
        elif choice == "Q":
            self.exit()
        else:
            print("Vous devez entrer un chiffre compris entre 1 et 3")
            self.menu()
    
    def categories_menu(self):
        """method who display all categories"""
        all_categories = self.dbreading.get_all_categories()
        self.dbreading.display_categories(all_categories)
        choiceC = input('Choisisez une catégorie:')

        if choiceC == "A":
            self.menu()
        elif choiceC == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.products_menu(choiceC)

    def products_menu(self, choiceC):
        """method who display all products of a catagory"""
        all_products = self.dbreading.get_products_category(choiceC)
        self.dbreading.display_products(all_products)
        choiceP = input("Choisissez un produit parmi la liste en indiquant son numéro de produit:")

        if choiceP == "A":
            self.menu()
        elif choiceP == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.get_all_substitute(choiceC, choiceP)

    def get_all_substitute(self, choiceC, choiceP):
        """method who display all subsitutes"""
        all_substitute = self.dbreading.get_all_substitute(choiceC, choiceP)
        self.dbreading.display_all_substitute(all_substitute)
        choiceS = input("Choisissez un substitut parmi la liste en indiquant son numéro de produit:")

        if choiceS == "A":
            self.menu()
        elif choiceS == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.one_substitute(choiceS)

    def one_substitute(self, choiceS):
        """Method who display the substitute choice and ask to the user if he/she wants to save it"""
        self.dbreading.one_substitute(choiceS)
        save = input('Souhaitez vous en enregistrer ce produit? (O pour Oui, N pour Non)')

        if save == "A":
            self.menu()
        elif save == "N" or "Q":
            print("A bientôt!")
            self.exit()
        elif save == "O":
            self.database.add_favorite(choiceS)
            print("produit sauvegardé")
            #self.menu()




    def exit(self):
        """Method to get out of the loop"""
        self.running = False


def main():
    test = Interface()
    test.menu()

if __name__ == "__main__":
    main()