from database import db
from datetime import datetime, UTC


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id_usuario = db.Column(db.Integer, primary_key=True)

    id_rol = db.Column(
        db.Integer,
        db.ForeignKey("roles.id_rol"),
        nullable=False
    )

    correo = db.Column(db.String(255), unique=True, nullable=False)

    telefono = db.Column(db.String(20))

    contrasena_hash = db.Column(db.String(255), nullable=False)

    fecha_registro = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC)
    )

    rol = db.relationship(
        "Rol",
        back_populates="usuarios"
    )

    paciente = db.relationship(
        "Paciente",
        back_populates="usuario",
        uselist=False
    )

    medico = db.relationship(
        "Medico",
        back_populates="usuario",
        uselist=False
    )

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "correo": self.correo,
            "telefono": self.telefono,
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None,
            "rol": self.rol.nombre_rol if self.rol else None
        }

    def __repr__(self):
        return f"<Usuario {self.correo}>"