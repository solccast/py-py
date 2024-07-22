from flask import Blueprint
from src.controllers.ciudades_controller import get_ciudad

ciudades = Blueprint('ciudades', __name__)

@ciudades.route('/ciudad')
def obtenerPaises():
    return get_ciudad()