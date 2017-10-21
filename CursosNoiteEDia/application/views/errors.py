# -*- coding: utf-8 -*-
from flask import redirect, render_template, url_for
from application.app import app


@app.errorhandler(401)
def unauthorized(error):
    return redirect(url_for('mod_login.login'))


@app.errorhandler(404)
def page_not_found(error):
    code = '404'
    error = u'Oops! Página não encontrada.'
    return render_template('error.html', error=error, code=code)


@app.errorhandler(405)
def method_not_allowed(error):
    code = '405'
    error = u'Oops! Método não permitido'
    return render_template('error.html', error=error, code=code)


@app.errorhandler(500)
def internal_server_error(error):
    code = '500'
    error = u'Oops! Erro interno no servidor'
    return render_template('error.html', error=error, code=code)


def error_personalized(error, code):
    return render_template('error.html', error=error, code=code)
