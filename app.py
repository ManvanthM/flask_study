from flask import Flask, request, render_template, redirect, url_for, flash, session
import os

from dotenv import load_dotenv
from users.routes import users_bp
from products.routes import products_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def home():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
    