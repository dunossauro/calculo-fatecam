# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view


home_app = Bottle()


@home_app.route('/')
@jinja2_view('index.html')
def index():
    return {'get_url': home_app.get_url}


@home_app.route('/dev')
@jinja2_view('dev.html')
def dev():
    return {'get_url': home_app.get_url}

@home_app.route('/ajuda')
@jinja2_view('ajuda.html')
def ajuda():
        return dict(title = 'Ajuda')

@home_app.route('/sobre')
@jinja2_view('sobre.html')
def sobre():
    return {'get_url': home_app.get_url}
