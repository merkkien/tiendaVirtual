from .db import db
from datetime import datetime

class Categoria(db.Model):
    categoriaId = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)

categoria=Categoria()