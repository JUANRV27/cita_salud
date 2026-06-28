from database import db


class Rol(db.Model):
    __tablename__ = "roles"

    id_rol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(50), unique=True, nullable=False)

    usuarios = db.relationship(
        "Usuario",
        back_populates="rol",
        lazy=True
    )
    
    def to_dict(self):
        return {
            "id": self.id_rol,
            "nombre": self.nombre_rol
        }

    def __repr__(self):
        return f"<Rol {self.nombre_rol}>"