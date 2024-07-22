from flask import jsonify, request

def get_pais():
    print(request.get_json())
    pais={
        "nombre":"Argentina",
        "estrellas": 3,
        "copas":16
    }
    return jsonify(pais)
