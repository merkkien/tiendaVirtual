from .db import db
from datetime import datetime

class Cliente(Usuario):
    clienteId = db.Column(db.Integer, primary_key=True)
    telefono = db.Column(db.String, nullable=False)
    direccion = db.Column(db.String, nullable=False)

cliente=Cliente()