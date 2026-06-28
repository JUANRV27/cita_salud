from database import db


class Paciente(db.Model):
    __tablename__ = "pacientes"

    id_paciente = db.Column(db.Integer, primary_key=True)

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id_usuario"),
        unique=True,
        nullable=False
    )

    nombres = db.Column(db.String(100), nullable=False)

    apellidos = db.Column(db.String(100), nullable=False)

    dni = db.Column(db.String(8), unique=True, nullable=False)

    usuario = db.relationship(
        "Usuario",
        back_populates="paciente"
    )

    citas = db.relationship(
        "Cita",
        back_populates="paciente",
        lazy=True
    )
    def to_dict(self):
        return {
            "id_paciente": self.id_paciente,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "dni": self.dni,
            "usuario": self.usuario.correo if self.usuario else None
        }

    def __repr__(self):
        return f"<Paciente {self.nombres} {self.apellidos}>"