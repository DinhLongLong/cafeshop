import math

from flask import Flask
from flask import render_template, request
from saleapp import app, dao


@app.context_processor
def inject_categories():
    categories = dao.get_categories()

    return {"categories": categories}


@app.route("/")
def index():
    cate_id = request.args.get('q')
    key = request.args.get('key')
    page = request.args.get('page', default=1, type=int)
    products = dao.get_products(cate_id, key)

    per_page = 4
    offset = (page - 1) * per_page
    total_items = len(products)
    total_pages = math.ceil(total_items / per_page)

    page_items = products[offset : offset + per_page]

    return render_template('index.html', products=page_items, cate_id=cate_id, total_pages=total_pages, page=page)


@app.route("/<int:product_id>")
def product_detail(product_id):
    product = dao.get_product_by_id(product_id)

    return render_template('product-detail.html', product=product)


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
