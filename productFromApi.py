import requests

class ProductFromApi:

    def __init__(self, category):
        self.category = category

    def get_json_by_category(self):
        url = 'https://fr.openfoodfacts.org/cgi/search.pl'
        parametres = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": self.category,
            "page_size": 150,
            "json": 1
            }

        request = requests.get(url, parametres)
        data = request.json()
        #print(data.keys())
        #print(data['products'])
        keys = ['brands', 'product_name_fr', 'nutrition_grade_fr', 'stores']
        new_list =[]
        for element in data['products']:
            new_dict = {}
            for key in keys:
                new_dict[key] = element[key]
            new_list.append(new_dict)         

        print(new_list)


def main():
    test_yaourts = ProductFromApi('yaourts')
    test_yaourts.get_json_by_category()


if __name__ == "__main__":
    main()
