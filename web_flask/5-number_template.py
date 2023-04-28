#!/usr/bin/python3
"""Script that starts a Flask web application:
web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Returns a given string
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a given string
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """
    Displays C followed by the value of the text variable
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """
    Displays Python followed by the value of the text variable
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """
    Displays “n is a number” only if n is an integer
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """
    Displays an HTML page only if n is an integer
    """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page only if n is an integer and indicates whether n is even or odd
    """
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template("6-number_odd_or_even.html", n=n, odd_or_even="even")
        else:
            return render_template("6-number_odd_or_even.html", n=n, odd_or_even="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
