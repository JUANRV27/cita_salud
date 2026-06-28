from models.medico import Medico
from models.usuario import Usuario
from models.especialidad import Especialidad


ROL_MEDICO = 2


def validar_usuario(id_usuario):

    usuario = Usuario.query.get(id_usuario)

    if usuario is None:
        return {
            "error": "El usuario no existe."
        }, 404

    return None


def validar_usuario_es_medico(id_usuario):

    usuario = Usuario.query.get(id_usuario)

    if usuario.id_rol != ROL_MEDICO:
        return {
            "error": "El usuario no tiene el rol de médico."
        }, 400

    return None


def validar_usuario_no_registrado(id_usuario):

    medico = Medico.query.filter_by(
        id_usuario=id_usuario
    ).first()

    if medico:
        return {
            "error": "El usuario ya está registrado como médico."
        }, 409

    return None


def validar_especialidad(id_especialidad):

    especialidad = Especialidad.query.get(
        id_especialidad
    )

    if especialidad is None:
        return {
            "error": "La especialidad no existe."
        }, 404

    return None


def validar_cmp_unico(cmp):

    medico = Medico.query.filter_by(
        colegiatura_cmp=cmp
    ).first()

    if medico:
        return {
            "error": "La colegiatura CMP ya está registrada."
        }, 409

    return None


def validar_cmp_actualizacion(id_medico, cmp):

    medico = Medico.query.filter_by(
        colegiatura_cmp=cmp
    ).first()

    if medico and medico.id_medico != id_medico:
        return {
            "error": "La colegiatura CMP ya está registrada."
        }, 409

    return None