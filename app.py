from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')  # Renders the login.html page


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')  # Renders the homepage.html page


if __name__ == '__main__':
    app.run(debug=True)
