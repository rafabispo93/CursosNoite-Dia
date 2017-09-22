from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String, unique=True)
    senha = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, usuario, senha, email):
        self.usuario = usuario
        self.senha = senha
        self.email = email

    def __repr__(self):
        return '<User %s>' % self.usuario

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    carga_horaria = db.Column(db.Integer)
    descricao = db.Column(db.String)
