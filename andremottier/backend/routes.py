from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user
from andremottier.backend import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/site-map')
@login_required
def site_map():
    #site_map = [item.string for item in list(current_app.url_map.iter_rules())]
    site_map = [(item.rule, item.methods, item.endpoint) for item in current_app.url_map.iter_rules()]
    #site_map = dir(list(current_app.url_map.iter_rules())[0])
    return render_template('site-map.html', site_map=site_map)
