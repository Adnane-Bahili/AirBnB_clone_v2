#!/usr/bin/python3
"""Starts the Flask web application"""
from flask import Flask
from flask import render_template

prgrm = Flask(__name__)
prgrm.jinja_env.trim_blocks = True
prgrm.jinja_env.lstrip_blocks = True


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


@prgrm.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays 'n is a number', when '<n>' is an 'int'"""
    return "{} is a number".format(n)


@prgrm.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """displays an HTML page, when '<n>' is an 'int'"""
    return render_template("5-number.html", n=n)


@prgrm.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """displays an HTML page, when '<n>' is an 'int'.
        Page would state whether <n> is an odd or even number"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    prgrm.run(host="0.0.0.0")
