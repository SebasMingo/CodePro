from models import db # Para interactuar con los modelos de la base de datos
from flask import Flask 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mis_notas.db"

app.config["SECRET_KEY"]='aaa'
db.init_app(app) #inicializa la aplicacion flask con la configuracion de SQLAlchemy

with app.app_context():
    db.create_all()