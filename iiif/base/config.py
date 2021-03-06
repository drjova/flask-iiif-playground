"""Config app."""
import os


class Config(object):

    """General config."""

    EXTENSIONS = [
        'iiif.extensions.assets',
        'iiif.extensions.cache',
        'iiif.extensions.collect',
        'iiif.extensions.debug',
        'iiif.extensions.restful',
        'iiif.extensions.iiif',
    ]

    PACKAGES = [
        'iiif.base'
    ]

    PACKAGES_EXCLUDE = []
    CACHE_TYPE = 'simple'


class ProdConfig(Config):

    """Production config."""


class HerokuConfig(Config):

    """Heroku config."""

    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    COLLECT_STORAGE = 'flask.ext.collect.storage.file'


class DevConfig(Config):

    """Dev config."""

    DEBUG = True
    ASSETS_DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))

    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = False
    COLLECT_STORAGE = 'flask_collect.storage.link'
