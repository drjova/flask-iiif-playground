"""Init Extension."""

from flask_iiif import IIIF

iiif = IIIF()


def uuid_to_source(uuid):
    """Full path of specified file."""
    if uuid == "huge":
        return '/Users/drjova/Public/native.jpg'
    else:
        return '/Users/drjova/Public/Space Bus.jpg'


def setup_app(app):
    """Init the extension with app context."""
    iiif.init_app(app)
    api = app.extensions['restful']
    iiif.init_restful(api)
    iiif.uuid_to_image_opener_handler(uuid_to_source)
    app.config['IIIF_CACHE_HANDLER'] = 'iiif.extensions.cache:cache'
    return app
