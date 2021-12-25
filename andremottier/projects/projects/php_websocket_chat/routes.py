from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

chat_server_php = Blueprint(
    name='chat_page', 
    import_name=__name__,
    static_folder='static',
    static_url_path=f'/static',
    template_folder='templates',
    url_prefix='/php-chat-server',
    root_path='/var/www/dev.andremottier.com/andremottier/projects/projects/php_websocket_chat'
)

chat_server_client = Blueprint(
    name='php_chat_client', 
    import_name=__name__,
    static_folder='static',
    static_url_path=f'/static',
    template_folder='/var/www/dev.andremottier.com/lib/PHP-Websockets/',
    url_prefix='/client',
    root_path='/var/www/dev.andremottier.com/lib/PHP-Websockets/'
)
chat_server_php.register_blueprint(chat_server_client)

@chat_server_php.route('/')
@login_required
def index():
    return render_template(
        'project.html',
        project_title="PHP WebSocket Chat Server",
        content_main=client(),
        scripts=[url_for(f'projects.chat_page.php_chat_client.static', filename='script.js')],
        styles=[url_for(f'projects.chat_page.php_chat_client.static', filename='style.css')],
    )

@chat_server_client.route('/')
@login_required
def client():
    return render_template('client.html')