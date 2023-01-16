#!/usr/bin/python3
"""
a script that starts a Flask web application
and must be listening on 0.0.0.0, port 5000
routes:
		/ - will display "Hello HBNB"
		/hbnb - displays "HBNB"
		/c/<text> - display C followed by the value
		/python/<text> - display python followed by the value
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """
    display just a text
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    display hbnb
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
    display “C ”
    followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """
    display “Python ”,
    followed by the value of the text variable
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    app.url_map.strict_slashes = False
