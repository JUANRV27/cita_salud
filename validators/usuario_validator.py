from models.rol import Rol
from models.usuario import Usuario


def validar_rol(id_rol):

    rol = Rol.query.get(id_rol)

    if rol is None:
        return {
            "error": "El rol no existe."
        }, 404

    return None


def validar_correo_unico(correo):

    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario:
        return {
            "error": "El correo ya está registrado."
        }, 409

    return None


def validar_correo_unico_actualizacion(id_usuario, correo):
    """
    Verifica que el correo no esté siendo utilizado por otro usuario.
    """

    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario and usuario.id_usuario != id_usuario:
        return {
            "error": "El correo ya está registrado."
        }, 409

    return None