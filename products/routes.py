from flask import Blueprint

products_bp = Blueprint(
    "products",
    __name__,url_prefix='/products'
)

@products_bp.route("/")
def products():
    return "Products Page"

@products_bp.route("/electronics")
def electronics():
    return "Electronics Page"

@products_bp.route("/clothing")
def clothing():
    return "Clothing Page"
