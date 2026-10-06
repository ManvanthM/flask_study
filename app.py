from flask import Flask, request , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return f"""
        <h1>Contact</h1>
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>Message: {message}</p>
        """

    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
    