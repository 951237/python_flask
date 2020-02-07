from flask import Flask, render_template    

app = Flask(__name__)


@app.route('/')
@app.route('/home')     # home 페이지
def home():
    return '<h1>Home page</h1>'

@app.route('/about')    # about 페이
def about():
    return '<h1>About page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
