from bottle import Bottle, jinja2_view, post, request, redirect, error

# -------------- Controle das views de erro
error = Bottle(True)

"""
### --------------  Página de Erro   -------------- ###
"""

# -------------- Página: Erro_0 - Expo
@error.route('/error_0')
@jinja2_view('error.html')
def error_0():
    return dict(out="Função exponencial não recebe valores negativos", title="ERRO")

# -------------- Página: Erro_0 - Log
@error.route('/error_1')
@jinja2_view('error.html')
def error_0():
    return dict(out="Função logarítma não recebe bases negativas ou iguais a zero", title="ERRO")
