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


if __name__ == "__main__":
    prgrm.run(host="0.0.0.0")
