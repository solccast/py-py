from flask import jsonify

def get_ciudad():
    data = {
        "nombre": "Buenos Aires",
        "capital": "La Plata"
    }
    return jsonify(data)