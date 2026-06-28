from database import db


class HistorialNotificacion(db.Model):
    __tablename__ = "historial_notificaciones"

    id_notificacion = db.Column(db.Integer, primary_key=True)

    id_cita = db.Column(
        db.Integer,
        db.ForeignKey("citas.id_cita"),
        nullable=False
    )

    fecha_envio = db.Column(db.DateTime)

    estado_envio = db.Column(
        db.String(30),
        nullable=False
    )

    cita = db.relationship(
        "Cita",
        back_populates="notificaciones"
    )
    def to_dict(self):
        return {
            "id_notificacion": self.id_notificacion,
            "id_cita": self.id_cita,
            "fecha_envio": self.fecha_envio.isoformat() if self.fecha_envio else None,
            "estado_envio": self.estado_envio
        }

    def __repr__(self):
        return f"<Notificacion {self.id_notificacion}>"