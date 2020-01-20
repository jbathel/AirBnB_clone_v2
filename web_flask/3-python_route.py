#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    text = text.replace("_", " ")
    return 'C %s' % (text)


@app.route('/python/<text>')
def python(text):
    python_text = text.replace("_", " ")
    return 'Python %s' % (python_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    strict_slashes = False
