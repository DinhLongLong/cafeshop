import json


def get_categories():
    with open('data/categories.json', encoding='UTF-8') as f:
        categories = json.load(f)

    return categories


def get_products(cate_id = None, key = None,):
    with open('data/products.json', encoding='UTF-8') as f:
        products = json.load(f)

    if cate_id != None:
        products = [prod for prod in products if prod["cate_id"].__eq__(int(cate_id))]

    if key != None:
        products = [prod for prod in products if key in (prod["name"])]

    # products = products[offset : offset + per_page]

    return products


def get_product_by_id(id):
    with open('data/products.json', encoding='UTF-8') as f:
        products = json.load(f)

        for prod in products:
            if prod["id"].__eq__(id):
                return prod



