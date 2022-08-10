from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Substantion(db.Model):
    __tablename__ = 'grls'

    id = db.Column(db.Integer, primary_key=True)
    drugname = db.Column(db.String(255))
    commonname = db.Column(db.String(255))
