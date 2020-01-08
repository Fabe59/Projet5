from dbreading import DbReading

class Interface:

    def __init__(self):
        self.running = True
        self.dbreading = DbReading()
        self.dbreading.connect()


    def menu(self):
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
        all_categories = self.dbreading.get_all_categories()
        self.dbreading.display_categories(all_categories)
        choice = input('Choisisez une catégorie:')

        if choice == "A":
            self.menu()
        elif choice == "Q":
            print("A bientôt!")
            self.exit()
        else:
            self.products_menu(choice)

    def products_menu(self, choice):
        all_products = self.dbreading.get_products_category(choice)
        self.dbreading.display_products(all_products)
        choice = input()

        if choice == "1":
            print("Vous avez choisi : produit1")
        elif choice == "2":
            print("Vous avez choisi : produit2")
        elif choice == "3":
            print("Vous avez choisi : produit3")
        elif choice == "4":
            self.menu()
        elif choice == "5":
            print("A bientôt!")
            self.exit()
        else:
            print("Vous devez entrer un chiffre correpondant au numéro du produit")
            self.products_menu()

    def exit(self):
        self.running = False


def main():
    test = Interface()
    test.menu()

if __name__ == "__main__":
    main()