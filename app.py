from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route("/users")
def users():
    return "This is users page"

@app.route("/user/<int:id>")
def profile(id):
    return f"This is {id} profile page"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Rupees {amount}"

@app.route("/string/<string:name>")
def name(name):
    return f"My name is {name}"

@app.route("/file/<path:file_path>")
def files(file_path):
    return f"This is {file_path} file path"


if __name__ == '__main__':
    app.run(debug=True)
    