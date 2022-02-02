#!/usr/bin/python3
"""Starts Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Return string at the root route"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0:5000')
