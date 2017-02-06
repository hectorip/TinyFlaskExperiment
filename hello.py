from flask import Flask

# Esto es para que tome el nombre del módulo y localizar dependencias
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask!"

# Decorador que indica la ruta, función a ejecutar cuando la ruta es llamada
@app.route("/faq")
def faq():
    # Lo que la función regresa es lo que la ruta devolverá
    return "Trying my own route"

# No correr accidentalmente este archivo si es importado
if __name__ == "__main__":
    app.run()