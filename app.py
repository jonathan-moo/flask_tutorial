from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index(name="Jonathan"):
    name = request.args.get('name',name)
    return "Hello from {}".format(name)

@app.route("/get_example")
# A GET request example
# Extracts 'name' URL parameter
def get_example(name="Jonathan"):
    name = request.args.get('name',name)
    return "Hello from {}".format(name)

app.run(debug=True, port=8000, host='127.0.0.1')