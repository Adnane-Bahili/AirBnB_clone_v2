#!/usr/bin/python3
"""Starts the Flask web application"""
from flask import Flask

prgrm = Flask(__name__)


@prgrm.route("/", strict_slashes=False)
def hello_hbnb():
    """displays 'Hello HBNB!' message"""
    return "Hello HBNB!"


@prgrm.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays ''HBNB' message"""
    return "HBNB"


@prgrm.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays 'C', followed by the value of the '<text>'' variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@prgrm.route("/python", strict_slashes=False)
@prgrm.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """displays 'Python', followed by the value of the '<text>'' variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    prgrm.run(host="0.0.0.0")
