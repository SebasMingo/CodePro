from models import db # Para interactuar con los modelos 
#de la base de datos
from flask import Flask
app = Flask(__name__)
#Una Uri(Uniforma Resource Identifier) de base de datos es una cadena de texto que especifica
#la ubicacion y de los detalles de conexion 
#para la base de datos que queremos usar en nuestra aplicacion
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mis_notas.db"

app.config["SECRET_KEY"] = 'aaabbbcccddd'

db.init_app(app) #inicializa la aplicacion flask 
#con la configuracion de SQLALchemy

with app.app_context():
    db.create_all()