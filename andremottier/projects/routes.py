from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

name = 'projects'
projects = Blueprint(
    name=name, 
    import_name=__name__,
    static_folder='static',
    static_url_path=f'/static',
    url_prefix='/projects',
    template_folder='templates',
    root_path='/var/www/dev.andremottier.com/andremottier/projects'
)

@projects.route('/')
@login_required
def index():
    return render_template(
        'showcase.html',
    )
