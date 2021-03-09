
from flask import Blueprint,request,json
from controllers.VentaController import ventacontroller

front = Blueprint("front", __name__)

@front.route('/', methods=['GET'])
def home():
    return ventacontroller.index()

@front.route('/about', methods=['GET'])
def about():
    return ventacontroller.about()