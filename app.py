from flask import Flask, request , render_template, redirect, url_for,flash

app = Flask(__name__)

app.secret_key = 'change-this-in-production'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name","").strip()
        email = request.form.get("email","").strip()
        age = request.form.get("age","").strip()

        if not name:
            flash("Name is required","danger")
            return redirect(url_for("contact"))
        if not email:
            flash("Email is required","danger")
            return redirect(url_for("contact"))
        if not age:
            flash("Age is required","danger")
            return redirect(url_for("contact"))
        if not age.isdigit():
            flash("Age must be a number","danger")
            return redirect(url_for("contact"))
        
        #flash("Registration Successful","success")
        # redirect to success page
        return redirect(url_for("success"))
        
        
    return render_template("contact.html")

@app.route('/success')
def success():
    return "Registration Successful"

if __name__ == '__main__':
    app.run(debug=True)
    