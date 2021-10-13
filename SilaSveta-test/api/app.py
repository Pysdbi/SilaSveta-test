#!/usr/bin/python3
import json

from flask import Flask

app = Flask(__name__)


@app.route('/')
def task1():
    with open('task1-data.json', 'r') as f:
        return json.loads(f.read())


if __name__ == '__main__':
    app.run(debug=True)
