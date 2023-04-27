#!/usr/bin/python3
"""Script that starts a Flask web application.
The application must be listening on 0.0.0.0, port 5000.
Routes:
    - /: Displays 'Hello HBNB!'
    - /hbnb: Displays 'HBNB'
    - /c/<text>: Displays 'C ' followed by the value of the text variable,
                 with underscores replaced with spaces
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """Displays 'C ' followed by the value of the text variable,
    with underscores replaced with spaces"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
