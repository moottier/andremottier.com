from flask import Blueprint
from andremottier.projects.projects.php_websocket_chat.routes import chat_server_php as chat_server_php_blueprint
from andremottier.projects.projects.image_resizer.routes import image_resizer as image_resizer_blueprint

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
projects.register_blueprint(chat_server_php_blueprint)
projects.register_blueprint(image_resizer_blueprint)