# This project just collect the data from the user and update the user. 🥹
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home is here"

if __name__ == '__main__':
    app.run()