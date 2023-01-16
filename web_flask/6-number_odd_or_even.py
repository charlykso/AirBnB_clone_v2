#!/usr/bin/python3
"""
a script that starts a Flask web application
and must be listening on 0.0.0.0, port 5000
routes : 
		/ - will display "Hello HBNB"
		/hbnb - displays "HBNB"
		/c/<text> - display C followed by the value
		/python/<text> - display python followed by the value
		/number/<n> -
		/number_template/<n> -
		/number_odd_or_even/<n>: display HTML page; display odd/even info
"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


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


@app.route('/number/<int:n>')
def text_if_int(n):
    """
    display “n is a number”
    only if n is an integer
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    display a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
