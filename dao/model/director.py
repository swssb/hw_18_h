# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)

# Пример
from marshmallow import Schema, fields
from setup_db import db


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


