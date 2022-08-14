from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

db = SQLAlchemy()


class Substantion(db.Model):
    __tablename__ = 'grls'
    id = db.Column(db.Integer, primary_key=True)
    commonname = db.Column(db.String(255))
    drugname = db.Column(db.String(255))


def base_search(src):
    res = Substantion.query.filter(
        or_(Substantion.commonname.contains(src),
            Substantion.drugname.contains(src))
    ).all()
    res_list = [item.commonname for item in res]
    return list(set(res_list))
