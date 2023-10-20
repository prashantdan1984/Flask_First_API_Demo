from app import app

@app.route("/product/add")
def product_add():
    return "This is a product add screen."