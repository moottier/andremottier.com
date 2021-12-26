from flask import render_template
from flask_login import login_required
from andremottier.projects import projects

@projects.route('/')
@login_required
def index():
    return render_template(
        'showcase.html',
    )
