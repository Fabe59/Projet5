import requests


class CategoryFromApi:

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


def main():
    Category = CategoryFromApi()
    Category.get_categories()


if __name__ == "__main__":
    main()
