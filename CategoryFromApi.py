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
        #print(data)
        for elt in data['tags'][:10]:
            print(elt)


def main():
    Category = CategoryFromApi()
    Category.get_json_category()


if __name__ == "__main__":
    main()