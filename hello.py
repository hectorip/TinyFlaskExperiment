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


@app.route("/echo")
def echo():
    response_string = "Recibí: "
    for k, v in request.iteritems():
        response_string += "%s: %s," % (k, v) 
    return response_string
# No correr accidentalmente este archivo si es importado
if __name__ == "__main__":
    app.run()