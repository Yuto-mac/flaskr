import os
import re

from flask import Flask, request, redirect, url_for
from flask.wrappers import Request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    from . import db
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    
    @app.route('/userProfile')
    def profile():
        name = request.args.get('name','')
        print(name)
        if name=="yuto":
            return dict(name='yuto', nums=100000)
        else:
            return dict(name='nono name', nums=19392)



    """
    @app.route('/admin')
    def hello_admin():
        return 'hello admin'

    @app.route('/guest/<guest>')
    def hello_guest(guest):
        return f'hello {guest}'

    @app.route('/user/<name>')
    def hello_user(name):
        if name == 'admin':
            return redirect(url_for('hello_admin'))
        else:
            return redirect(url_for('hello_guest', guest = name))
    """
    return app
