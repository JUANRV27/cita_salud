from models.paciente import Paciente
from models.usuario import Usuario

ROL_PACIENTE = 1


def validar_usuario(id_usuario):

    usuario = Usuario.query.get(id_usuario)

    if usuario is None:
        return {
            "error": "El usuario no existe."
        }, 404

    return None


def validar_usuario_es_paciente(id_usuario):

    usuario = Usuario.query.get(id_usuario)

    if usuario.id_rol != ROL_PACIENTE:
        return {
            "error": "El usuario no tiene el rol de paciente."
        }, 400

    return None


def validar_usuario_no_registrado(id_usuario):

    paciente = Paciente.query.filter_by(
        id_usuario=id_usuario
    ).first()

    if paciente:
        return {
            "error": "El usuario ya está registrado como paciente."
        }, 409

    return None


def validar_dni_unico(dni):

    paciente = Paciente.query.filter_by(
        dni=dni
    ).first()

    if paciente:
        return {
            "error": "El DNI ya está registrado."
        }, 409

    return None


def validar_dni_actualizacion(id_paciente, dni):

    paciente = Paciente.query.filter_by(
        dni=dni
    ).first()

    if paciente and paciente.id_paciente != id_paciente:
        return {
            "error": "El DNI ya está registrado."
        }, 409

    return None