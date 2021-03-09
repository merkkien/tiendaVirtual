from .db import db
from datetime import datetime

class Envio(db.Model):
    envioId = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String, nullable=False)
    costo = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String, nullable=False)
    idDepartamento = db.Column(db.Integer, nullable=False)
    idMunicipio = db.Column(db.Integer, nullable=False)
    ventaId = db.Column(db.Integer, db.ForeignKey('venta.ventaId'),
    nullable=False)

envio=Envio()