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


@app.route('/python', strict_slashes=False)
def pythonDefault():
    """ Define Python page """
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def pythondisplayPage(text):
    """ Define python page """
    if not text:
        return redirect(url_for('/python'))
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def numDisplay(n):
    """ Define a dyamic page """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
