from flask import Blueprint, render_template

mod_app = Blueprint('mod_app', __name__)


@mod_app.route('/')
def home_mod():
    return render_template('index.html', title='Index')
