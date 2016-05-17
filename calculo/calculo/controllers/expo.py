# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request, redirect
from wtforms import Form, fields, SubmitField, FloatField

from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN

expo = Bottle()

"""
### --------------  Form Cadastro -------------- ###
"""
class Cadastro(Form):
    x = FloatField('x')
    butt = SubmitField('OK!')

@expo.route('/expo')
@jinja2_view('expo.html')
def get():
    return dict(titulo="Função Exponencial",form = Cadastro())

@expo.post('/expo')
@jinja2_view('saida.html')
def post():

    form = Cadastro(request.POST)   # ----- POST METHOD
    ex = form.x.data

    #derivada = a

    if ex < 0:
        return redirect('/error_0')

    x_range = range(-100, 100)

    y = [ x**ex for x in x_range]

    p = figure(title="Exponencial", x_axis_label='x', y_axis_label='y')
    p.line(x_range, y, legend="Linha", line_width=2)

    graph_line = file_html(p, CDN)

    return dict(bokeh_line=graph_line,
                texto="Exponencial")
                #derivada=derivada)
