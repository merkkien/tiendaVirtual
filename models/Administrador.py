from .db import db
from datetime import datetime

class Administrador(Usuario):
    administradorId = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String, nullable=False)

administrador=Administrador()