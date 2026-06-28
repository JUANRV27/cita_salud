from database import db


class HorarioDisponible(db.Model):
    __tablename__ = "horarios_disponibles"

    id_horario = db.Column(db.Integer, primary_key=True)

    id_medico = db.Column(
        db.Integer,
        db.ForeignKey("medicos.id_medico"),
        nullable=False
    )

    id_sede = db.Column(
        db.Integer,
        db.ForeignKey("sedes.id_sede"),
        nullable=False
    )

    fecha = db.Column(db.Date, nullable=False)

    hora_inicio = db.Column(db.Time, nullable=False)

    hora_fin = db.Column(db.Time, nullable=False)

    estado_disponible = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    medico = db.relationship(
        "Medico",
        back_populates="horarios"
    )

    sede = db.relationship(
        "Sede",
        back_populates="horarios"
    )

    cita = db.relationship(
        "Cita",
        back_populates="horario",
        uselist=False
    )

    def to_dict(self):
        return {
            "id_horario": self.id_horario,
            "fecha": self.fecha.isoformat(),
            "hora_inicio": str(self.hora_inicio),
            "hora_fin": str(self.hora_fin),
            "estado_disponible": self.estado_disponible,
            "medico": f"{self.medico.nombres} {self.medico.apellidos}" if self.medico else None,
            "sede": self.sede.nombre_sede if self.sede else None
        }

    def __repr__(self):
        return f"<Horario {self.fecha}>"