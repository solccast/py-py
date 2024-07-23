from src.database.database_config import db
from sqlalchemy import Integer, String

class Country(db.Model):
    __tablename__="countries"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), unique=True, nullable=False)
    name = db.Column(db.String(50))
    continent = db.Column(db.String(50))
    population = db.Column(db.Integer)
    capital = db.Column(db.Integer, db.ForeignKey("cities.id")) #Aca va el nombre de la tabla, no del modelo. No confundir con el cities declarado abajo
    cities = db.relationship('City', backref='country') #esto define la relacion a muchas ciudades


#Un país tiene una capital que es una ciudad.
#Una ciudad pertenece a un país. 
