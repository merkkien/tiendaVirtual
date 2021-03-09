from .db import db
from datetime import datetime
from .Categoria import categoria

class Producto(db.Model):
    productoId = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    especificaciones = db.Column(db.String, nullable=False)
    marca = db.Column(db.String, nullable=False)
    inventario  = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    categoriaId = db.Column(db.Integer, db.ForeignKey('categoria.categoriaId'),
        nullable=False)
    categoria = db.relationship('Categoria',
        backref=db.backref('productos', lazy=True))

producto=Producto()