#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print 'Hello HBNB' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Print 'C is <text>' """
    text = text.replace("_", " ")
    return 'C %s' % (text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Print 'Python is <text>' """
    text = text.replace("_", " ")
    return 'Python %s' % (text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ Print 'n is a number' only if n is an integer """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
