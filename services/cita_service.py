from database import db
from datetime import datetime, UTC
from models.cita import Cita
from models.horario_disponible import HorarioDisponible
from models.historial_notificacion import HistorialNotificacion

from validators.common import (
    validar_campos_requeridos,
    ejecutar_validaciones
)

from validators.cita_validator import (
    validar_paciente,
    validar_horario,
    validar_horario_disponible,
    validar_horario_sin_cita
)

from utils.database import (
    obtener_o_error,
    commit_or_rollback
)

CAMPOS_REQUERIDOS = [
    "id_paciente",
    "id_horario",
    "tiene_seguro"
]


def obtener_citas():
    citas = Cita.query.all()
    return [cita.to_dict() for cita in citas]


def obtener_cita_por_id(id_cita):
    cita, error = obtener_o_error(
        Cita,
        id_cita,
        "Cita"
    )

    if error:
        return error

    return cita.to_dict(), 200


def crear_cita(datos):
    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(datos, CAMPOS_REQUERIDOS),
        lambda: validar_paciente(datos["id_paciente"]),
        lambda: validar_horario(datos["id_horario"]),
        lambda: validar_horario_disponible(datos["id_horario"]),
        lambda: validar_horario_sin_cita(datos["id_horario"])
    ])

    if error:
        return error

    horario = HorarioDisponible.query.get(datos["id_horario"])

    cita = Cita(
        id_paciente=datos["id_paciente"],
        id_horario=datos["id_horario"],
        tiene_seguro=datos["tiene_seguro"],
        estado_cita="confirmada",
        fecha_reserva=datetime.now(UTC)
    )

    horario.estado_disponible = False

    db.session.add(cita)

    error = commit_or_rollback(
        "No fue posible crear la cita."
    )

    if error:
        return error

    return cita.to_dict(), 201


def actualizar_cita(id_cita, datos):
    cita, error = obtener_o_error(
        Cita,
        id_cita,
        "Cita"
    )

    if error:
        return error

    cita.tiene_seguro = datos.get(
        "tiene_seguro",
        cita.tiene_seguro
    )

    cita.estado_cita = datos.get(
        "estado_cita",
        cita.estado_cita
    )

    error = commit_or_rollback(
        "No fue posible actualizar la cita."
    )

    if error:
        return error

    return cita.to_dict(), 200


def cancelar_cita(id_cita):
    cita, error = obtener_o_error(
        Cita,
        id_cita,
        "Cita"
    )

    if error:
        return error

    horario = cita.horario

    cita.estado_cita = "cancelada"

    if horario:
        horario.estado_disponible = True

    error = commit_or_rollback(
        "No fue posible cancelar la cita."
    )

    if error:
        return error

    return {
        "mensaje": "Cita cancelada correctamente."
    }, 200


def eliminar_cita(id_cita):
    cita, error = obtener_o_error(
        Cita,
        id_cita,
        "Cita"
    )

    if error:
        return error

    if cita.horario:
        cita.horario.estado_disponible = True

    HistorialNotificacion.query.filter_by(
        id_cita=id_cita
    ).delete()
    
    db.session.delete(cita)

    error = commit_or_rollback(
        "No fue posible eliminar la cita."
    )

    if error:
        return error

    return {
        "mensaje": "Cita eliminada correctamente."
    }, 200