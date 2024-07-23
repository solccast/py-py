from src.database.database_config import db
from sqlalchemy import Integer, String

class Usuario(db.Model): #Esto es lo que permite crear tablas
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(50))
    dni = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<Nombre %r >" %self.nombre
