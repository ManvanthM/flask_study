from flask import Flask, request , render_template

app = Flask(__name__)

@app.route('/')
def home():
    name="Manvanth"
    courses=['Python','Flask','Django']
    city="Mysore"
    price=5000
    student={"Name":"Manvanth","age":21,"gender":"Male"}
    return render_template("index.html",name=name,courses=courses,city=city,price=price,student=student)

if __name__ == '__main__':
    app.run(debug=True)
    