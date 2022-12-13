from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/login")
def login():
    return "<H1>Hello Sampath!!</H1>"