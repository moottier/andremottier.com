from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from andremottier import db

main = Blueprint(
    name='main',
    import_name=__name__,
    root_path='/var/www/dev.andremottier.com/andremottier/backend',
    template_folder='templates',
    static_folder='../static'
)

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
name = 'chat_server_php'
chat_server_php = Blueprint(
    name=name, 
    import_name=__name__,
    static_folder='static',
    static_url_path=f'/static/{name}',
    template_folder='',
    root_path='/var/www/dev.andremottier.com/lib/PHP-Websockets'
)

@chat_server_php.route('/chat-server')
def show():
    content_main = render_template('client.html')
    return render_template(
        'project.html',
        project_title="PHP WebSocket Chat Server",
        content_main=content_main,
        scripts=[url_for(f'{name}.static', filename='script.js')],
        styles=[url_for(f'{name}.static', filename='style.css')],
    )
    #return '<p>Routed</p>'