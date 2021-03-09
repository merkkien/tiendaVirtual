from .db import db
from datetime import datetime

class Devoluciones(db.Model):
    devolucionId = db.Column(db.Integer, primary_key=True)
    fechaDevolucion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    motivoDevolucion = db.Column(db.String, nullable=False)
    ventaId = db.Column(db.Integer, db.ForeignKey('venta.ventaId'),
        nullable=False)

devoluciones=Devoluciones()