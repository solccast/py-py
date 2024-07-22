from .paisesRoute import paises as paisesRoute
from .ciudadesRoute import ciudades as ciudadesRoute

def register_blueprints(app):
    app.register_blueprint(paisesRoute, url_prefix='/country')
    app.register_blueprint(ciudadesRoute, url_prefix='/city')