# -*- coding: utf-8 -*-
from bottle import Bottle

from .controllers.home import home_app
from .controllers.primeiro_grau import pri_grau
from .controllers.segundo_grau import seg_grau
from .controllers.expo import expo
from .controllers.log import log
from .controllers.error import error
from .controllers.limite import limite


Routes = Bottle()
# App to render / (home)
Routes.merge(home_app)
Routes.merge(pri_grau)
Routes.merge(seg_grau)
Routes.merge(expo)
Routes.merge(log)
Routes.merge(error)
Routes.merge(limite)
