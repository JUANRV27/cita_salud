from database import db
from datetime import datetime
from models.horario_disponible import HorarioDisponible

from validators.common import (
    validar_campos_requeridos,
    ejecutar_validaciones
)

from validators.horario_validator import (
    validar_medico,
    validar_sede,
    validar_horas,
    validar_horario_repetido
)

from utils.database import (
    obtener_o_error,
    commit_or_rollback
)

CAMPOS_REQUERIDOS = [
    "id_medico",
    "id_sede",
    "fecha",
    "hora_inicio",
    "hora_fin"
]


def obtener_horarios():

    horarios = HorarioDisponible.query.all()

    return [
        horario.to_dict()
        for horario in horarios
    ]


def obtener_horario_por_id(id_horario):

    horario, error = obtener_o_error(
        HorarioDisponible,
        id_horario,
        "Horario"
    )

    if error:
        return error

    return horario.to_dict(), 200


def crear_horario(datos):
    try:
        datos["fecha"] = datetime.strptime(
            datos["fecha"],
            "%Y-%m-%d"
        ).date()

        datos["hora_inicio"] = datetime.strptime(
            datos["hora_inicio"],
            "%H:%M"
        ).time()

        datos["hora_fin"] = datetime.strptime(
            datos["hora_fin"],
            "%H:%M"
        ).time()

    except ValueError:
        return {
            "error": "Formato inválido. Usa fecha YYYY-MM-DD y horas HH:MM."
        }, 400


    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(
            datos,
            CAMPOS_REQUERIDOS
        ),
        lambda: validar_medico(
            datos["id_medico"]
        ),
        lambda: validar_sede(
            datos["id_sede"]
        ),
        lambda: validar_horas(
            datos["hora_inicio"],
            datos["hora_fin"]
        ),
        lambda: validar_horario_repetido(
            datos["id_medico"],
            datos["fecha"],
            datos["hora_inicio"]
        )
    ])

    if error:
        return error

    horario = HorarioDisponible(
        id_medico=datos["id_medico"],
        id_sede=datos["id_sede"],
        fecha=datos["fecha"],
        hora_inicio=datos["hora_inicio"],
        hora_fin=datos["hora_fin"],
        estado_disponible=True
    )

    db.session.add(horario)

    error = commit_or_rollback(
        "No fue posible crear el horario."
    )

    if error:
        return error

    return horario.to_dict(), 201


def actualizar_horario(id_horario, datos):

    horario, error = obtener_o_error(
        HorarioDisponible,
        id_horario,
        "Horario"
    )

    if error:
        return error

    horario.fecha = datos.get(
        "fecha",
        horario.fecha
    )

    horario.hora_inicio = datos.get(
        "hora_inicio",
        horario.hora_inicio
    )

    horario.hora_fin = datos.get(
        "hora_fin",
        horario.hora_fin
    )

    horario.estado_disponible = datos.get(
        "estado_disponible",
        horario.estado_disponible
    )

    error = commit_or_rollback(
        "No fue posible actualizar el horario."
    )

    if error:
        return error

    return horario.to_dict(), 200


def eliminar_horario(id_horario):

    horario, error = obtener_o_error(
        HorarioDisponible,
        id_horario,
        "Horario"
    )

    if error:
        return error

    db.session.delete(horario)

    error = commit_or_rollback(
        "No fue posible eliminar el horario."
    )

    if error:
        return error

    return {
        "mensaje": "Horario eliminado correctamente."
    }, 200