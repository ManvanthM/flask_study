from flask import Flask,jsonify,request,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy(app)


@app.route('/')
def home():
    return "Home Page"

@app.route('/create-user',methods=["POST"])
def create_user():
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")
    age=data.get("age")
    user=User(name=name,email=email,age=age)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message":"User Created Successfully",
    "name":name,"email":email,"age":age})

@app.route('/get-user',methods=["GET"])
def get_users():
    users=User.query.all()
    user_list=[]
    for user in users:
        user_list.append({
            "id":user.id,
            "name":user.name,
            "email":user.email,
            "age":user.age
        })
    return jsonify(user_list)

@app.route("/get-user/<int:id>",methods=["GET"])
def get_user(id):
    user=User.query.get(id)
    if user is None:
        return jsonify({"message":"User Not Found"}),404
    return jsonify({
        "id":user.id,
        "name":user.name,
        "email":user.email,
        "age":user.age
    })

@app.route("/users-form")
def users_form():
    users=User.query.all()
    return render_template("user.html",users=users)

@app.route("/users/<int:id>",methods=["PATCH"])
def update_user(id):
    data=request.get_json()
    user=db.get_or_404(User,id)
    if "name" in data:
        user.name=data.get("name")
    if "email" in data:
        user.email=data.get("email")
    if "age" in data:
        user.age=data.get("age")
    db.session.commit()
    return jsonify({"message":"User Updated Successfully",
    "name":user.name,"email":user.email,"age":user.age})

@app.route("/users/<int:id>",methods=["DELETE"])
def delete_user(id):
    user=db.get_or_404(User,id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message":"User Deleted Successfully"}) 

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(80),unique=True,nullable=False)
    age=db.Column(db.Integer,nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
