import requests

class CategoryFromApi:

    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/categories/'

    def get_json_category(self):
        parametres = {
            "action": "process",
            "json": 1
            }

        request = requests.get(self.url, parametres)
        data = request.json()
        cat_list = []
        for elt in data['tags'][:10]:
            cat_list.append(elt)
        #print(cat_list)


def main():
    Category = CategoryFromApi()
    Category.get_json_category()


if __name__ == "__main__":
    main()
