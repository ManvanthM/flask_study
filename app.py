from flask import Flask, request, render_template, redirect, url_for, flash, session
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = 'change-this-in-production'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['GET', 'POST'])
@app.route('/uplode', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # 1. Check if the file part is in the request
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
            
        file = request.files['file']
        
        # 2. Check if the user didn't select a file
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
            
        if file:
            # 3. Secure the filename to prevent directory traversal attacks
            filename = secure_filename(file.filename)
            
            # 4. Save the file safely
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            flash('File uploaded successfully', 'success')
            return redirect(url_for('upload'))
            
    return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

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
    