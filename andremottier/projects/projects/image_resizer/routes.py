from flask import flash, render_template, url_for, jsonify, request, send_file
import io, sys
from andremottier.projects.projects.image_resizer import image_resizer
from .image_resizer import resizer

from PIL import Image

def validate_request():
    if not hasattr(request, 'content_length'): return False
    content_length = request.content_length or 0
    
    if not (0 < content_length < 5000000): return False

    if not hasattr(request, 'form'): return False
    width = request.form.get('width') or '0'
    height = request.form.get('height') or '0'
    
    if not (width.isnumeric() and height.isnumeric()): return False
    if not ((0 < len(width) <= 4) and (0 < len(height) <= 4)): return False

    if not request.files.getlist('file'): return False
    if not len(request.files.getlist('file')) == 1: return False
    
    file = request.files.getlist('file')[0]
    if not resizer.get_PIL_format_from_mimetype(file.mimetype): return False
    
    return True

@image_resizer.route('/')
def index():
    return render_template(
        'resizer.html',
        project_title="Image Resizer",
        scripts=[
            "https://kit.fontawesome.com/1863f96517.js",
             url_for(f'projects.image_resizer.static', filename='main.js')],
        styles=[],
    )

def get_link(innerHTML, href, attributes=None):
    """Return an <A> element with values passed
    Attributes not implemented""" 
    return f'<a href={href}>{innerHTML}</a>'

@image_resizer.route('/submit', methods=['POST'])
def submit():
    if validate_request():
        # print(validate_request)
        # issue = get_link('issue', 'https://github.com/moottier/image_resizer/issues')
        err_msg = ""
        # flash(err_msg)    # need ajax
        return err_msg, 500
    else:
        file = request.files.getlist('file')[0]
        size = (int(request.form['width']), int(request.form['height']))
        img = resizer.resize(io.BytesIO(file.read()), size)
        format = resizer.get_PIL_format_from_mimetype(file.mimetype)
        
        img_io_out = io.BytesIO()
        resizer.save_image(img, img_io_out, format=format)
        img_io_out.seek(0)
        
        fn = file.filename or f'Resized Image.{format}'
        fn = resizer.get_new_name(fn, size)
        return send_file(img_io_out, download_name=fn, mimetype=file.mimetype)