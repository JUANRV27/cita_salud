from database import db


class Medico(db.Model):
    __tablename__ = "medicos"

    id_medico = db.Column(db.Integer, primary_key=True)

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id_usuario"),
        unique=True,
        nullable=False
    )

    id_especialidad = db.Column(
        db.Integer,
        db.ForeignKey("especialidades.id_especialidad"),
        nullable=False
    )

    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    colegiatura_cmp = db.Column(db.String(20), unique=True, nullable=False)

    usuario = db.relationship(
        "Usuario",
        back_populates="medico"
    )

    especialidad = db.relationship(
        "Especialidad",
        back_populates="medicos"
    )

    horarios = db.relationship(
        "HorarioDisponible",
        back_populates="medico",
        lazy=True
    )

    def to_dict(self):
        return {
            "id_medico": self.id_medico,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "colegiatura_cmp": self.colegiatura_cmp,
            "correo": self.usuario.correo if self.usuario else None,
            "especialidad": self.especialidad.nombre_especialidad if self.especialidad else None
        }

    def __repr__(self):
        return f"<Medico {self.nombres} {self.apellidos}>"