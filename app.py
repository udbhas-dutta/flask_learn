from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///taskapp.db"
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/products")
def products():
    return "<h1>This is the products page</h1>"

if __name__ == "__main__":
    app.run(debug=True)