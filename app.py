from flask import Flask, request , render_template, redirect, url_for,flash,session

app = Flask(__name__)

app.secret_key = 'change-this-in-production'

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

@app.route('/test-500')
def test_500():
    result=1/0 
    return str(result)  


@app.route("/login")
def login():
    session["username"]="Manvanth"
    return "Login successful"    
@app.route("/dashboard")
def dashboard():
    username=session.get("username")
    if not username:
        return "Please Login to access dashboard"
    return f"hello {username} , your are in dashboard"

@app.route("/logout")
def logout():
    session.pop("username",None)
    return "Logged out successfully"

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
    