# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request
from wtforms import Form, fields, SubmitField, FloatField

from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN

seg_grau = Bottle()

"""
### --------------  Form Cadastro -------------- ###
"""
class Cadastro(Form):
    a = FloatField('a')
    b = FloatField('b')
    c = FloatField('c')
    butt = SubmitField('OK!')

@seg_grau.route('/2grau')
@jinja2_view('2grau.html')
def get():
    return dict(titulo="Função de segundo grau",form = Cadastro())

@seg_grau.post('/2grau')
@jinja2_view('saida.html')
def post():

    form = Cadastro(request.POST)   # ----- POST METHOD
    a = form.a.data
    b = form.b.data
    c = form.c.data

    derivada = a

    x_range = range(-100, 100)

    y = [(a*x**2)+(x*b)+c for x in x_range]

    p = figure(title="Segundo grau", x_axis_label='x', y_axis_label='y')
    p.line(x_range, y, legend="Linha", line_width=2)

    graph_line = file_html(p, CDN)

    return dict(bokeh_line=graph_line,
                texto="2º Grau",
                derivada=derivada)
