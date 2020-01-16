import requests


class CategoryFromApi:
    """Class to download the top ten categories""" 

    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/categories/'

    def get_categories(self):
        parametres = {
            "action": "process",
            "json": 1
            }

        request = requests.get(self.url, parametres)
        data = request.json()
        cat_list = []
        ordered_cat_list = []
        for elt in data['tags'][:10]:
            cat_list.append(elt)
        for category in cat_list:
            ordered_cat_list.append(category['name'])
        return ordered_cat_list
