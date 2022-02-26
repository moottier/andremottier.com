from flask import render_template, url_for
from andremottier.projects.projects.image_resizer import image_resizer

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