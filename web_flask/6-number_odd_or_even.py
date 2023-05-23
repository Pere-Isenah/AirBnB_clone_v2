#!/usr/bin/python3
"""
A Simple flask application with multiple routes.
"""

from flask import Flask, render_template

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

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Define the /number/<int:n> route.
    """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Define the /number/<n> route.

    Args:
        n (int): The number parameter provided in the route.

    Returns:
        str: A formatted message indicating that the value is a number.
    """
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
     """
    Determine if a number is odd or even.

    Args:
        n (int): The number to check.

    Returns:
        str: A rendered HTML template with the result.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
