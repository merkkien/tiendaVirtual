from .db import db
from datetime import datetime

class Cupon(db.Model):
    cuponId = db.Column(db.Integer, primary_key=True)
    fechaCreacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fechaVencimiento = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    clienteId = db.Column(db.Integer, db.ForeignKey('cliente.clienteId'),
        nullable=True)
    
cupon=Cupon()