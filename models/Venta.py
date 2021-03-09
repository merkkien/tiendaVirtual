from .db import db
from datetime import datetime

class Venta(db.Model):
    ventaId = db.Column(db.Integer, primary_key=True)
    fechaCreacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fechaEnvio = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    estado = db.Column(db.String, nullable=False)
    medioPago = db.Column(db.String, nullable=False)
    valorTotal = db.Column(db.Float, nullable=False)
    clienteId = db.Column(db.Integer, db.ForeignKey('cliente.clienteId'),
        nullable=True)
        
venta=Venta()