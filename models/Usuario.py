from .db import db
from datetime import datetime

class Usuario(db.Model):
    __abstract__ = True
    nombre = db.Column(db.String, nullable=False)
    correoElectronico = db.Column(db.String, nullable=False)
    contraseña = db.Column(db.String, nullable=False)
    loginEstado = db.Column(db.String, nullable=False)
    fechaRegistro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

usuario=Usuario()