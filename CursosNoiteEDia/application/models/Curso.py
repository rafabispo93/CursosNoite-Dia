from app.app import db


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    carga_horaria = db.Column(db.Integer)
    descricao = db.Column(db.String)
