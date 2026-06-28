from database import db

from models.usuario import Usuario

from validators.common import (
    validar_campos_requeridos,
    validar_formato_correo,
    validar_password,
    validar_telefono,
    ejecutar_validaciones
)

from validators.usuario_validator import (
    validar_rol,
    validar_correo_unico,
    validar_correo_unico_actualizacion
)

from utils.database import (
    obtener_o_error,
    commit_or_rollback
)

CAMPOS_REQUERIDOS = [
    "id_rol",
    "correo",
    "telefono",
    "contrasena_hash"
]


def obtener_usuarios():

    usuarios = Usuario.query.all()

    return [usuario.to_dict() for usuario in usuarios]


def obtener_usuario_por_id(id_usuario):

    usuario, error = obtener_o_error(
        Usuario,
        id_usuario,
        "Usuario"
    )

    if error:
        return error

    return usuario.to_dict(), 200


def crear_usuario(datos):

    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(
            datos,
            CAMPOS_REQUERIDOS
        ),
        lambda: validar_formato_correo(
            datos["correo"]
        ),
        lambda: validar_telefono(
            datos["telefono"]
        ),
        lambda: validar_password(
            datos["contrasena_hash"]
        ),
        lambda: validar_rol(
            datos["id_rol"]
        ),
        lambda: validar_correo_unico(
            datos["correo"]
        )
    ])

    if error:
        return error

    usuario = Usuario(
        id_rol=datos["id_rol"],
        correo=datos["correo"],
        telefono=datos["telefono"],
        contrasena_hash=datos["contrasena_hash"]
    )

    db.session.add(usuario)

    error = commit_or_rollback(
        "No fue posible crear el usuario."
    )

    if error:
        return error

    return usuario.to_dict(), 201


def actualizar_usuario(id_usuario, datos):

    usuario, error = obtener_o_error(
        Usuario,
        id_usuario,
        "Usuario"
    )

    if error:
        return error

    validaciones = []

    if "correo" in datos:

        validaciones.append(
            lambda: validar_formato_correo(
                datos["correo"]
            )
        )

        validaciones.append(
            lambda: validar_correo_unico_actualizacion(
                id_usuario,
                datos["correo"]
            )
        )

    if "telefono" in datos:

        validaciones.append(
            lambda: validar_telefono(
                datos["telefono"]
            )
        )

    if "id_rol" in datos:

        validaciones.append(
            lambda: validar_rol(
                datos["id_rol"]
            )
        )

    error = ejecutar_validaciones(validaciones)

    if error:
        return error

    usuario.correo = datos.get(
        "correo",
        usuario.correo
    )

    usuario.telefono = datos.get(
        "telefono",
        usuario.telefono
    )

    usuario.id_rol = datos.get(
        "id_rol",
        usuario.id_rol
    )

    error = commit_or_rollback(
        "No fue posible actualizar el usuario."
    )

    if error:
        return error

    return usuario.to_dict(), 200


def eliminar_usuario(id_usuario):

    usuario, error = obtener_o_error(
        Usuario,
        id_usuario,
        "Usuario"
    )

    if error:
        return error

    db.session.delete(usuario)

    error = commit_or_rollback(
        "No fue posible eliminar el usuario."
    )

    if error:
        return error

    return {
        "mensaje": "Usuario eliminado correctamente."
    }, 200