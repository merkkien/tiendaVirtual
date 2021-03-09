from .db import db
from datetime import datetime
from .Producto import producto
from .Venta import venta

class DetalleVenta(db.Model):
    detalleId = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    valorSinIva = db.Column(db.Float, nullable=False)
    valorIva = db.Column(db.Float, nullable=False)
    valorDescuento = db.Column(db.Float, nullable=False)
    productoId = db.Column(db.Integer, db.ForeignKey('producto.productoId'),
        nullable=False)
    producto = db.relationship('Producto',
        backref=db.backref('detalles', lazy=True))
    ventaId = db.Column(db.Integer, db.ForeignKey('venta.ventaId'),
        nullable=False)
    venta = db.relationship('Venta',
        backref=db.backref('detallaventas', lazy=True))

detalleVenta=DetalleVenta()