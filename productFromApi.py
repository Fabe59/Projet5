import requests

class ProductFromApi:

    def __init__(self):
        self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'

    def get_product(self, cat):
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
        #print(data.keys())
        #print(data['products'])
        keys = ['brands', 'product_name_fr', 'nutrition_grade_fr', 'stores']
        new_list =[]
        for element in data['products']:
            new_dict = {}
            for key in keys:
                new_dict[key] = element[key]
            new_list.append(new_dict)         
        #return new_list
        print(new_list)


def main():
    test = ProductFromApi()
    test.get_product('snacks')


if __name__ == "__main__":
    main()