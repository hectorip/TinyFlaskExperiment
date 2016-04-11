from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask!"

@app.route("/faq")
def faq():
    return "Trying my own route"

if __name__ == "__main__":
    app.run()