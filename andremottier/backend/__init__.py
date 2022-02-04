from flask import Blueprint

main = Blueprint(
    name='main',
    import_name=__name__,
    static_folder='static',
    static_url_path=f'/static',
    url_prefix='/',
    template_folder='templates',
    root_path='/var/www/dev.andremottier.com/andremottier/backend'
)
auth = Blueprint('auth', __name__)
