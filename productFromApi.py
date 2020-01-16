import requests


class ProductFromApi:

    def __init__(self):
        """API url"""
        self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'

    def get_products(self, cat):
        """Search parameters"""
        parametres = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": cat,
            "page_size": 1,
            "json": 1
            }

        request = requests.get(self.url, parametres)
        data = request.json()
        """Selected keywords"""
        keys = ['id', 'brands', 'product_name_fr',
                'nutrition_grade_fr', 'stores', 'url']
        products_list = []
        for element in data['products']:
            product = {}
            for key in keys:
                product[key] = element.get(key)
            if all(product.values()):
                """Test if all 'products' keys have a value"""
                products_list.append(product)
        return products_list
