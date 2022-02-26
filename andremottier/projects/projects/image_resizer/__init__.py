from flask import Blueprint

image_resizer = Blueprint(
    name='image_resizer', 
    import_name=__name__,
    static_folder='static',
    static_url_path=f'/static',
    template_folder='templates',
    url_prefix='/image-resizer',
    root_path='/var/www/dev.andremottier.com/andremottier/projects/projects/image_resizer'
)
