from flask import Flask
from  src.routes import register_blueprints
from src.database.database_config import db
from src.models import Usuario, Country, City
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


#with app.app_context():
#    db.create_all()

register_blueprints(app)

if __name__ == "__main__":
    print('---Aplicacion en funcionamiento---')
    app.run(debug=True, port=5000)
    