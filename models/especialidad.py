from database import db


class Especialidad(db.Model):
    __tablename__ = "especialidades"

    id_especialidad = db.Column(db.Integer, primary_key=True)
    nombre_especialidad = db.Column(db.String(100), unique=True, nullable=False)

    medicos = db.relationship(
        "Medico",
        back_populates="especialidad",
        lazy=True
    )
    
    def to_dict(self):
        return {
            "id_especialidad": self.id_especialidad,
            "nombre_especialidad": self.nombre_especialidad
        }

    def __repr__(self):
        return f"<Especialidad {self.nombre_especialidad}>"