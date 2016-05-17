# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request, redirect
from wtforms import Form, fields, SubmitField, FloatField

from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN

import math

log = Bottle()

"""
### --------------  Form Cadastro -------------- ###
"""
class Cadastro(Form):
    base = FloatField('base')
    butt = SubmitField('OK!')

@log.route('/log')
@jinja2_view('log.html')
def get():
    return dict(titulo="Função Logarítmica",form = Cadastro())

@log.post('/log')
@jinja2_view('saida.html')
def post():

    form = Cadastro(request.POST)   # ----- POST METHOD
    base = form.base.data

    print(type(base));print(base)

    #derivada = a

    if base <= 0:
        return redirect('/error_1')

    x_range = range(1,100)

    y = [ math.log(x, base) for x in x_range]

    p = figure(title="Logarítmica", x_axis_label='x', y_axis_label='y')
    p.line(x_range, y, legend="Linha", line_width=2)

    graph_line = file_html(p, CDN)

    return dict(bokeh_line=graph_line,
                texto="Logarítmica")
                #derivada=derivada)
