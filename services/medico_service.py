from database import db

from models.medico import Medico

from validators.common import (
    validar_campos_requeridos,
    ejecutar_validaciones
)

from validators.medico_validator import (
    validar_usuario,
    validar_usuario_es_medico,
    validar_usuario_no_registrado,
    validar_especialidad,
    validar_cmp_unico,
    validar_cmp_actualizacion
)

from utils.database import (
    obtener_o_error,
    commit_or_rollback
)

CAMPOS_REQUERIDOS = [
    "id_usuario",
    "id_especialidad",
    "nombres",
    "apellidos",
    "colegiatura_cmp"
]


def obtener_medicos():

    medicos = Medico.query.all()

    return [medico.to_dict() for medico in medicos]


def obtener_medico_por_id(id_medico):

    medico, error = obtener_o_error(
        Medico,
        id_medico,
        "Médico"
    )

    if error:
        return error

    return medico.to_dict(), 200


def crear_medico(datos):

    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(
            datos,
            CAMPOS_REQUERIDOS
        ),
        lambda: validar_usuario(
            datos["id_usuario"]
        ),
        lambda: validar_usuario_es_medico(
            datos["id_usuario"]
        ),
        lambda: validar_usuario_no_registrado(
            datos["id_usuario"]
        ),
        lambda: validar_especialidad(
            datos["id_especialidad"]
        ),
        lambda: validar_cmp_unico(
            datos["colegiatura_cmp"]
        )
    ])

    if error:
        return error

    medico = Medico(
        id_usuario=datos["id_usuario"],
        id_especialidad=datos["id_especialidad"],
        nombres=datos["nombres"],
        apellidos=datos["apellidos"],
        colegiatura_cmp=datos["colegiatura_cmp"]
    )

    db.session.add(medico)

    error = commit_or_rollback(
        "No fue posible crear el médico."
    )

    if error:
        return error

    return medico.to_dict(), 201


def actualizar_medico(id_medico, datos):

    medico, error = obtener_o_error(
        Medico,
        id_medico,
        "Médico"
    )

    if error:
        return error

    validaciones = []

    if "id_usuario" in datos:

        validaciones.append(
            lambda: validar_usuario(
                datos["id_usuario"]
            )
        )

        validaciones.append(
            lambda: validar_usuario_es_medico(
                datos["id_usuario"]
            )
        )

        if datos["id_usuario"] != medico.id_usuario:

            validaciones.append(
                lambda: validar_usuario_no_registrado(
                    datos["id_usuario"]
                )
            )

    if "id_especialidad" in datos:

        validaciones.append(
            lambda: validar_especialidad(
                datos["id_especialidad"]
            )
        )

    if "colegiatura_cmp" in datos:

        validaciones.append(
            lambda: validar_cmp_actualizacion(
                id_medico,
                datos["colegiatura_cmp"]
            )
        )

    error = ejecutar_validaciones(validaciones)

    if error:
        return error

    medico.id_usuario = datos.get(
        "id_usuario",
        medico.id_usuario
    )

    medico.id_especialidad = datos.get(
        "id_especialidad",
        medico.id_especialidad
    )

    medico.nombres = datos.get(
        "nombres",
        medico.nombres
    )

    medico.apellidos = datos.get(
        "apellidos",
        medico.apellidos
    )

    medico.colegiatura_cmp = datos.get(
        "colegiatura_cmp",
        medico.colegiatura_cmp
    )

    error = commit_or_rollback(
        "No fue posible actualizar el médico."
    )

    if error:
        return error

    return medico.to_dict(), 200


def eliminar_medico(id_medico):

    medico, error = obtener_o_error(
        Medico,
        id_medico,
        "Médico"
    )

    if error:
        return error

    db.session.delete(medico)

    error = commit_or_rollback(
        "No fue posible eliminar el médico."
    )

    if error:
        return error

    return {
        "mensaje": "Médico eliminado correctamente."
    }, 200