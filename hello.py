from flask import Flask

# Esto es para que tome el nombre del módulo y localizar dependencias
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask!"


@app.route("/faq")
def faq():
    return "Trying my own route"

# No correr accidentalmente este archivo si es importado
if __name__ == "__main__":
    app.run()