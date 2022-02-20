from flask import render_template, url_for
from flask_login import login_required
from andremottier.projects.projects.php_websocket_chat import chat_server_php, chat_server_client

@chat_server_php.route('/')
def index():
    return render_template(
        'project.html',
        project_title="PHP WebSocket Chat Server",
        content_main=client(),
        project_server_active=True,
        test="toast",
        scripts=[
            url_for(f'projects.chat_page.php_chat_client.static', filename='script.js')
            ,"https://kit.fontawesome.com/1863f96517.js"
            ],
        styles=[
                url_for(f'projects.chat_page.php_chat_client.static', filename='style.css')
                ,url_for(f'projects.chat_page.static', filename='css/style.css')
                ],
    )

@chat_server_client.route('/')
def client():
    return render_template('client.html')