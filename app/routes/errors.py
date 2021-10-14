from flask import Blueprint, render_template

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def handle_not_found(e):
    return render_template('404.html'), 404


@errors.app_errorhandler(500)
def handle_not_found(e):
    return render_template('500.html'), 500
