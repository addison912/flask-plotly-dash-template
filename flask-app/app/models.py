from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(512))
    organization = db.Column(db.String(128))
    # organization = db.relationship('Org', backref='user', lazy='True')
    role = db.Column(db.String(64), default="default")
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    verified = db.Column(db.Boolean, default=False)

    vcode = db.Column(db.String(64))

    @property
    def is_verified(self):
        return self.verified

    @property
    def get_domain(self):
        res = self.email[self.email.index('@') + 1:]
        return res

    def __str__(self):
        return self.id


# class App(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     app_name = db.Column(db.String(128), nullable=False)
#     path_prefix = db.Column(db.String(64))
#     roles = db.relationship('Role', lazy='subquery',
#         backref=db.backref('app', lazy=True))
#     def __str__(self):
#         return self.id


# class Org(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name=db.Column(db.String(64))
#     apps=db.relationship('App',
#         backref=db.backref('org', lazy=True))
#     users=db.Column(db.Integer, db.ForeignKey('user.id'),
#         nullable=False)
#     email_domain= db.Column(db.String(64), nullable=False)
#     def __str__(self):
#         return self.id


# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     organization = db.relationship('Orgs', backref='role', lazy='True')
#     def __str__(self):
#         return self.id
