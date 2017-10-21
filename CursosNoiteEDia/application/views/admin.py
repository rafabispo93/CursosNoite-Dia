from flask import Blueprint, render_template

mod_admin = Blueprint('mod_admin', __name__)


@mod_admin.route('/admin')
def admin():
    return render_template("admin.html")
