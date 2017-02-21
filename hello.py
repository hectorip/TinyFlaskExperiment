# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

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


@app.route("/html")
def html():
    return render_template("test1.html")


@app.route("/params/<param>")
def route_parameters(param):
    return render_template("templates_with_params.html", param=param)
# @app.route("/echo")
# def echo():
#     response_string = "Recibí: "
#     for k, v in request.iteritems():
#         response_string += "%s: %s," % (k, v) 
#     return response_string
# No correr accidentalmente este archivo si es importado
if __name__ == "__main__":
    app.run()