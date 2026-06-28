from database import db


class Cita(db.Model):
    __tablename__ = "citas"

    id_cita = db.Column(db.Integer, primary_key=True)

    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey("pacientes.id_paciente"),
        nullable=False
    )

    id_horario = db.Column(
        db.Integer,
        db.ForeignKey("horarios_disponibles.id_horario"),
        unique=True,
        nullable=False
    )

    tiene_seguro = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    estado_cita = db.Column(
        db.String(30),
        nullable=False
    )

    fecha_reserva = db.Column(db.DateTime)

    paciente = db.relationship(
        "Paciente",
        back_populates="citas"
    )

    horario = db.relationship(
        "HorarioDisponible",
        back_populates="cita"
    )

    notificaciones = db.relationship(
        "HistorialNotificacion",
        back_populates="cita",
        lazy=True
    )

    def to_dict(self):
        return {
            "id_cita": self.id_cita,
            "paciente": f"{self.paciente.nombres} {self.paciente.apellidos}" if self.paciente else None,
            "medico": (
                f"{self.horario.medico.nombres} {self.horario.medico.apellidos}"
                if self.horario and self.horario.medico else None
            ),
            "fecha": self.horario.fecha.isoformat() if self.horario else None,
            "hora_inicio": str(self.horario.hora_inicio) if self.horario else None,
            "tiene_seguro": self.tiene_seguro,
            "estado_cita": self.estado_cita,
            "fecha_reserva": self.fecha_reserva.isoformat() if self.fecha_reserva else None
        }
    def __repr__(self):
        return f"<Cita {self.id_cita}>"