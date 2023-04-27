#!/usr/bin/python3
"""This script starts a Flask web app"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display 'Hello HBNB' when GET request is sent to root."""
    return "Hello HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
