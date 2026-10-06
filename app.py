from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route("/users")
def users():
    return "This is users page"

@app.route("/user/<username>")
def profile(username):
    return f"This is {username} profile page"

@app.route("/student/<name>/<course>")
def student(name,course):
    return f"The student {name} is studying {course}"
    
if __name__ == '__main__':
    app.run(debug=True)
    