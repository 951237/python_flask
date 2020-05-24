from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        return render_template('index.html', graph='')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
