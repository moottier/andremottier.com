from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user
from andremottier.backend import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, page_title='Profile')

@main.route('/url-map')
@login_required
def url_map():
    url_map = [
        (item.rule, item.methods, item.endpoint) 
        for item in current_app.url_map.iter_rules()
        ]
    return render_template('url-map.html', url_map=url_map, page_title='Url Map')
