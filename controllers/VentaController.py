
from flask import request
from flask import render_template
from models.DetalleVenta import detalleVenta

class VentaController():

    def __init__(self):
        pass

    def index(self):
        ventas = detalleVenta.query.all()
        return render_template('index.html', title='Home', ventas=ventas)

    def about(self):
        return render_template('about.html', title='About')

ventacontroller=VentaController()

