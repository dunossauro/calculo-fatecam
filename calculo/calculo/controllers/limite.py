# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request
from wtforms import Form, fields, SubmitField, FloatField, StringField
from sympy import *

from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN

limite = Bottle()

"""
### --------------  Form Cadastro -------------- ###
"""
class Cadastro(Form):
    a = StringField('Função')
    b = FloatField('Tende a:')
    butt = SubmitField('OK!')

@limite.route('/lim')
@jinja2_view('lim.html')
def get():
    return dict(titulo="Limite de funções",form = Cadastro())

@limite.post('/lim')
@jinja2_view('saida_1.html')
def post():

    form = Cadastro(request.POST)   # ----- POST METHOD
    func = form.a.data
    tende = form.b.data

    x = Symbol('x')

    saida = limit(func, x, tende)

    return dict(derivada=func,bokeh_line=saida, texto="Limite")
