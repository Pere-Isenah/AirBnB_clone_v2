#!/usr/bin/python3
""" A Simple flask application with a single page """
from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Defines index page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Defines hbnb page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cdisplayPage(text):
    """ Define c page """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythondisplayPage(text="is cool"):
    """ Define python page """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
