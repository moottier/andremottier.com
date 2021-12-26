from flask import render_template, url_for
from flask_login import login_required
from andremottier.projects.projects.php_websocket_chat import chat_server_php, chat_server_client

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