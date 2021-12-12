from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/project/chat-server-php')
@login_required
def project(project_name='#blahblah'):
    return render_template('chat_server_php.html', project_name=project_name)


from flask import abort
from jinja2 import TemplateNotFound
chat_server_php = Blueprint(
    name='chat_server_php', 
    import_name=__name__,
    # static_folder='static',
    # static_url_path='chat-server/static'
    template_folder='',
    root_path='/var/www/dev.andremottier.com/PHP-Websockets'
)

@chat_server_php.route('/chat-server')
def show():
    #try:
    return render_template(f'client.html')
    # except TemplateNotFound:
    #     import sys
    #     #print("***TAG***: ", simple_page.static_folder, file=sys.stdout)
    #     abort(404)
