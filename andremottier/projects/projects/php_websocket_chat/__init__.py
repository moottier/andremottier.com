from flask import Blueprint

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