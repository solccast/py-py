from src.database.database_config import db
from sqlalchemy import Integer, String

class City(db.Model):
    __tablename__="cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    country_code = db.Column(db.Integer, db.ForeignKey("countries.id"), nullable=False)


