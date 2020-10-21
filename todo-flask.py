from flask import Flask  # import flask

app = Flask(__name__)  # create an app instance

@app.route("/")  # at the end point /
def hello():  # call method hello
    return "Hello World! This is test. Debugger mode is on"  # which returns "hello world"

@app.route("/api/index")
def getName(name):
    name = input("Please enter the name")
    return "THe provided name = " + name;

if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app