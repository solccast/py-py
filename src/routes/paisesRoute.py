from flask import Blueprint, jsonify
from src.controllers.paises_controller import get_pais

paises= Blueprint('paises', __name__)

@paises.route("/inicio")
def mensaje():
    print('Dentro de msg')
    return "ok"

@paises.route('/paises', methods=['GET'])
def listarPaises():
    data = {
        'country1': "Argentina",
        'country2': "Chile"
    }
    return jsonify(data), 200

@paises.route('/pais', methods=['GET'])
def obtenerPais():
    return get_pais()

#main.add_url_rule('/blabla', controlador)  