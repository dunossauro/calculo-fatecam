# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request
from wtforms import Form, fields, SubmitField, FloatField

from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN

pri_grau = Bottle()

"""
### --------------  Form Cadastro -------------- ###
"""
class Cadastro(Form):
    a = FloatField('a')
    b = FloatField('b')
    butt = SubmitField('OK!')

@pri_grau.route('/1grau')
@jinja2_view('1grau.html')
def get():
    return dict(titulo="Função de primeiro grau",form = Cadastro())

@pri_grau.post('/1grau')
@jinja2_view('saida.html')
def post():

    form = Cadastro(request.POST)   # ----- POST METHOD
    a = form.a.data
    b = form.b.data

    derivada = a

    x_range = range(-100, 100)

    y = [(x*a)+(b) for x in x_range]

    p = figure(title="Primeiro Grau", x_axis_label='x', y_axis_label='y')
    p.line(x_range, y, legend="Linha", line_width=2)

    graph_line = file_html(p, CDN)

    return dict(bokeh_line=graph_line,
                texto="1º Grau",
                derivada=derivada)
