class Menu:

    def __init__(self):
        self.running = True


    def menu(self):
        print("Bienvenue, que souhaitez faire?\n1 = Substituer un produit \n2 = Revoir les produits déjà substitués \n3 = Quitter")
        choice = input()

        if choice == "1":
            print("Vous avez choisi de substituer un produit.")
            self.categories_menu()
        elif choice == "2":
            print("Vous avez choisi de revoir vos produits subsitués")
        elif choice == "3":
            print("A bientôt!")
            self.exit()
        else:
            print("Vous devez entrer un chiffre compris entre 1 et 3")
            self.menu()
    
    def categories_menu(self):
        print("Veuillez maintenant choisir une catégorie: \n1 = Boissons \n2 = Yaourts \n3 = Pizzas \n4 = Retour au menu principal \n5 = Quitter")
        choice = input()

        if choice == "1":
            print("Vous avez choisi la catégorie : 'Boissons'")
            self.products_menu()
        elif choice == "2":
            print("Vous avez choisi la catégorie : 'Yaourts'")
            self.products_menu()
        elif choice == "3":
            print("Vous avez choisi la catégorie : 'Pizzas'")
            self.products_menu()
        elif choice == "4":
            self.menu()
        elif choice == "5":
            print("A bientôt!")
            self.exit()
        else:
            print("Vous devez entrer un chiffre au numéro de la catégorie")
            self.categories_menu()

    def products_menu(self):
        print("Veuillez choisir un produit de cette catégorie: \n1 = produit1 \n2 = produit2 \n3 = Produit3 \n4 = Retour au menu principal \n5 = Quitter")
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
    test = Menu()
    test.menu()

if __name__ == "__main__":
    main()