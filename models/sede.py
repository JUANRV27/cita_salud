from database import db


class Sede(db.Model):
    __tablename__ = "sedes"

    id_sede = db.Column(db.Integer, primary_key=True)

    nombre_sede = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)

    horarios = db.relationship(
        "HorarioDisponible",
        back_populates="sede",
        lazy=True
    )

    def to_dict(self):
        return {
            "id_sede": self.id_sede,
            "nombre_sede": self.nombre_sede,
            "direccion": self.direccion
        }

    def __repr__(self):
        return f"<Sede {self.nombre_sede}>"