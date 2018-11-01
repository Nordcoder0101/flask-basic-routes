from flask import Flask

app = Flask(__name__)

@app.route("./")
def index():
  return "Hello World"

@app.route("./")
def dojo():
  return "Dojo"

@app.route("/hi/<name>")
def hi(name):
    print(f"Hello {name}")
    return f"Hello {name}"

@app.route