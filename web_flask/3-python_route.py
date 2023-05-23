#!/usr/bin/python3
"""
A Simple flask application with multiple routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """
    Define index page.
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Define /hbnb route.
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """
    Define /c/<text> route.
    """
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    Define /python/ and /python/<text> routes.
    """
    return "Python {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
