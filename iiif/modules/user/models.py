"""User models."""

from quality.extensions.sqlalchemy import db


class User(db.Model):

    """Define the user model."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    github_access_token = db.Column(db.String(255))

    def __init__(self, github_access_token):
        """Init user."""
        self.github_access_token = github_access_token

    def is_authenticated(self):
        """User authenticated."""
        return True

    def is_active(self):
        """Active user."""
        return True

    def is_anonymous(self):
        """User anonymous."""
        return False

    def get_id(self):
        """Get id."""
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        """User represetnation."""
        return '<User %r>' % (self.username)
