from flask import render_template, url_for, jsonify, request, send_file
import io
from andremottier.projects.projects.image_resizer import image_resizer
from .image_resizer import resizer

from PIL import Image

def validate_request():
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

@image_resizer.route('/submit', methods=['POST'])
def submit():
    if not validate_request():
        pass    # error
    else:
        file = request.files.getlist('file')[0]
        size = (int(request.form['width']), int(request.form['height']))
        img = resizer.resize(io.BytesIO(file.read()), size)
        format = resizer.get_PIL_format_from_mimetype(file.mimetype)
        
        img_io_out = io.BytesIO()
        resizer.save_image(img, img_io_out, format=format)
        img_io_out.seek(0)
        
        return send_file(img_io_out, download_name=file.filename, mimetype=file.mimetype)