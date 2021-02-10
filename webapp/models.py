import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from webapp import app
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey


db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    child = relationship("Table")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,  password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "{}".format(self.username)


# class Table(db.Model):
#     parent_id = Column(Integer, ForeignKey('Users.id'))












# # from models import db  # shsell
# # db.create_all() #- створити базу

# if __name__ == '__main__':
#     u1 = Users(username='test')
#     u1.set_password('111222')
#     db.session.add(u1)
#     db.session.add_all([u1])
#     db.session.commit()
