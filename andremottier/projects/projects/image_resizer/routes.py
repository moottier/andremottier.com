from flask import render_template, url_for, jsonify, request, send_file
import io
from andremottier.projects.projects.image_resizer import image_resizer

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
        file = file.read()
        return send_file(io.BytesIO(file), download_name='new name.jpg')
        
    