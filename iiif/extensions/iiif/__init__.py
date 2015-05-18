"""Init Extension."""
import os

from flask_iiif import IIIF

iiif = IIIF()


def setup_app(app):
    """Init the extension with app context."""
    iiif.init_app(app)
    api = app.extensions['restful']
    iiif.init_restful(api)
    image_path = os.path.join(app.instance_path, 'images')

    def uuid_to_source(uuid):
        """Full path of specified file."""
        return os.path.join(image_path, uuid)
    iiif.uuid_to_image_opener_handler(uuid_to_source)
    app.config['IIIF_CACHE_HANDLER'] = 'iiif.extensions.cache:cache'
    return app
