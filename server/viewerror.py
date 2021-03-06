from flask import render_template
from . import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('./error/404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 302