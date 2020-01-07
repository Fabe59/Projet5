import requests


class ProductFromApi:

    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'

    def get_products(self, cat):
        parametres = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": cat,
            "page_size": 50,
            "json": 1
            }

        request = requests.get(self.url, parametres)
        data = request.json()
        keys = ['id', 'brands', 'product_name_fr', 'nutrition_grade_fr', 'stores']
        products_list = []
        for element in data['products']:
            product = {}
            for key in keys:
                product[key] = element.get(key)
            if all(product.values()):  # teste si toutes les clés de 'products' ont une valeur
                products_list.append(product)
        return products_list
        #print(products_list)
        
                        
def main():
    a = ProductFromApi()
    a.get_products("boissons")


if __name__ == "__main__":
    main()