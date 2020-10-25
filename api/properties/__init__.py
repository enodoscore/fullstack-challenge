import os

from flask import Flask
from .db import check_db, get_db_path


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=get_db_path(),
    )

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

    @app.route('/healthcheck')
    def healthcheck():
        """Ensure the DB is up otherwise API health is bad.."""
        if check_db():
            return '200'
        else:
            return '500'

    from . import service
    app.register_blueprint(service.bp)

    return app
