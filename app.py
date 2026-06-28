import os
from flask import Flask
from flask_cors import CORS
from config import Config
from database import db
from sqlalchemy import text
from models import *
from routes.roles import roles_bp
from routes.usuarios import usuarios_bp
from routes.sedes import sede_bp
from routes.medicos import medico_bp
from routes.pacientes import paciente_bp
from routes.horarios import horario_bp
from routes.citas import cita_bp
from routes.especialidades import especialidades_bp

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

db.init_app(app)

app.register_blueprint(
    roles_bp,
    url_prefix="/roles"
)

app.register_blueprint(
    usuarios_bp,
    url_prefix="/usuarios"
)

app.register_blueprint(
    sede_bp,
    url_prefix="/sedes"
)

app.register_blueprint(
    medico_bp,
    url_prefix="/medicos"
)

app.register_blueprint(
    paciente_bp,
    url_prefix="/pacientes"
)

app.register_blueprint(
    horario_bp,
    url_prefix="/horarios"
)

app.register_blueprint(
    cita_bp,
    url_prefix="/citas"
)

app.register_blueprint(
    especialidades_bp,
    url_prefix="/especialidades"
)

if __name__ == "__main__":
    app.run(        
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )

