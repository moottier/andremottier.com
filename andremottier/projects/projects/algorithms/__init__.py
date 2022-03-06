from flask import Blueprint

algorithms = Blueprint(
    name='algorithms', 
    import_name=__name__,
    static_folder='static',
    static_url_path=f'/static',
    template_folder='templates',
    url_prefix='/algorithms',
    root_path='/var/www/dev.andremottier.com/andremottier/projects/projects/algorithms'
)
