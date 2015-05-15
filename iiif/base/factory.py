"""Create the app."""
import os
import sys
import warnings

from flask import Flask, render_template

from flask_registry import (
    BlueprintAutoDiscoveryRegistry,
    ConfigurationRegistry,
    ExtensionRegistry,
    PackageRegistry,
    Registry
)


def create_app(instance_path="", env="prod"):
    """Create the app."""
    app_name = '.'.join(__name__.split('.')[0:2])

    instance_path = instance_path or os.path.join(
        sys.prefix, 'var', app_name + '-instance'
    )
    try:
        if not os.path.exists(instance_path):
            os.makedirs(instance_path)
    except Exception:
        pass
    app = Flask(
        app_name,
        instance_path=instance_path,
        instance_relative_config=True,
        static_folder=os.path.join(instance_path, 'static'),
    )

    app.config['ENV'] = env
    env_object = "iiif.base.config.{0}Config".format(
        env.capitalize()
    )
    app.config.from_object(env_object)

    app.config.from_envvar('iiif_ENV_SRC', silent=True)
    app.config.from_pyfile('application.cfg', silent=True)

    # Ignore slashes
    app.url_map.strict_slashes = False

    # register_secret_key
    register_secret_key(app)

    # Add the proxies
    Registry(app=app)
    app.extensions['registry'].update(
        packages=PackageRegistry(app)
    )
    app.extensions['registry'].update(
        extensions=ExtensionRegistry(app),
        blueprints=BlueprintAutoDiscoveryRegistry(app=app),
    )
    ConfigurationRegistry(app)
    _setup_app_errors(app)
    return app


def register_secret_key(app):
    """Register secret key."""
    SECRET_KEY = app.config.get('SECRET_KEY', 'abcdefg')

    if SECRET_KEY == 'abcdefg':
        warnings.warn(
            ("You might want to add a random secret key by running"
             "/n $ python manage.py secret"),
            UserWarning
        )
    app.config.update(
        SECRET_KEY=SECRET_KEY
    )


def _setup_app_errors(app):
    """Setup errors."""
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('error/500.html'), 500
