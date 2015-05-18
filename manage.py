#!/usr/bin/env python
import os
import sys

from iiif.base.factory import create_app

from flask_collect import Collect
from flask_script import Manager, Server, Shell, prompt_choices
from flask_script.commands import ShowUrls, Clean

env = os.environ.get('iiif_ENV', 'dev')
instance_path = ""
if env == "Heroku":
    instance_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'instance'
    )

app = create_app(instance_path=instance_path, env=env)

manager = Manager(app=app)
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command("shell", Shell())

collect = Collect()
collect.init_app(app)
collect.init_script(manager)


@manager.command
def debug():
    """Get dev settings."""
    print "Prefix: {0}".format(sys.prefix)
    print "Instance: {0}".format(app.instance_path)
    print "Static: {0}".format(app.static_folder)
    print "======================================="
    print app.config


@manager.command
def secret():
    """Generate secret key."""
    import string
    import random
    return ''.join(
        [
            random.choice(
                string.ascii_letters + string.digits
            )
            for dummy in range(0, 256)
        ]
    )

if __name__ == "__main__":
    manager.run()
