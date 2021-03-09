from .db import db
from datetime import datetime

class CarroCompra(db.Model):
    carroId = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    fechaAgrego = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    clienteId = db.Column(db.Integer, db.ForeignKey('cliente.clienteId'),
        nullable=True)

carroCompra=CarroCompra()