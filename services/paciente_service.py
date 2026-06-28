from database import db

from models.paciente import Paciente

from validators.common import (
    validar_campos_requeridos,
    ejecutar_validaciones
)

from validators.paciente_validator import (
    validar_usuario,
    validar_usuario_es_paciente,
    validar_usuario_no_registrado,
    validar_dni_unico,
    validar_dni_actualizacion
)

from utils.database import (
    obtener_o_error,
    commit_or_rollback
)

CAMPOS_REQUERIDOS = [
    "id_usuario",
    "nombres",
    "apellidos",
    "dni"
]


def obtener_pacientes():

    pacientes = Paciente.query.all()

    return [paciente.to_dict() for paciente in pacientes]


def obtener_paciente_por_id(id_paciente):

    paciente, error = obtener_o_error(
        Paciente,
        id_paciente,
        "Paciente"
    )

    if error:
        return error

    return paciente.to_dict(), 200


def crear_paciente(datos):

    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(
            datos,
            CAMPOS_REQUERIDOS
        ),
        lambda: validar_usuario(
            datos["id_usuario"]
        ),
        lambda: validar_usuario_es_paciente(
            datos["id_usuario"]
        ),
        lambda: validar_usuario_no_registrado(
            datos["id_usuario"]
        ),
        lambda: validar_dni_unico(
            datos["dni"]
        )
    ])

    if error:
        return error

    paciente = Paciente(
        id_usuario=datos["id_usuario"],
        nombres=datos["nombres"],
        apellidos=datos["apellidos"],
        dni=datos["dni"]
    )

    db.session.add(paciente)

    error = commit_or_rollback(
        "No fue posible crear el paciente."
    )

    if error:
        return error

    return paciente.to_dict(), 201


def actualizar_paciente(id_paciente, datos):

    paciente, error = obtener_o_error(
        Paciente,
        id_paciente,
        "Paciente"
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
            lambda: validar_usuario_es_paciente(
                datos["id_usuario"]
            )
        )

        if datos["id_usuario"] != paciente.id_usuario:

            validaciones.append(
                lambda: validar_usuario_no_registrado(
                    datos["id_usuario"]
                )
            )

    if "dni" in datos:

        validaciones.append(
            lambda: validar_dni_actualizacion(
                id_paciente,
                datos["dni"]
            )
        )

    error = ejecutar_validaciones(validaciones)

    if error:
        return error

    paciente.id_usuario = datos.get(
        "id_usuario",
        paciente.id_usuario
    )

    paciente.nombres = datos.get(
        "nombres",
        paciente.nombres
    )

    paciente.apellidos = datos.get(
        "apellidos",
        paciente.apellidos
    )

    paciente.dni = datos.get(
        "dni",
        paciente.dni
    )

    error = commit_or_rollback(
        "No fue posible actualizar el paciente."
    )

    if error:
        return error

    return paciente.to_dict(), 200


def eliminar_paciente(id_paciente):

    paciente, error = obtener_o_error(
        Paciente,
        id_paciente,
        "Paciente"
    )

    if error:
        return error

    db.session.delete(paciente)

    error = commit_or_rollback(
        "No fue posible eliminar el paciente."
    )

    if error:
        return error

    return {
        "mensaje": "Paciente eliminado correctamente."
    }, 200