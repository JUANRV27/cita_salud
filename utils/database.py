from database import db


def obtener_o_error(modelo, id_objeto, nombre_modelo):
    objeto = db.session.get(modelo, id_objeto)

    if objeto is None:
        return None, (
            {
                "error": f"{nombre_modelo} no encontrado."
            },
            404
        )

    return objeto, None


def guardar(objeto, mensaje_error="Error al guardar el registro."):
    db.session.add(objeto)
    return commit_or_rollback(mensaje_error)


def eliminar(objeto, mensaje_error="Error al eliminar el registro."):
    db.session.delete(objeto)
    return commit_or_rollback(mensaje_error)


def commit_or_rollback(mensaje_error="Error interno del servidor."):
    try:
        db.session.commit()
        return None

    except Exception as e:
        db.session.rollback()
        print("ERROR DB:", e)

        return {
            "error": mensaje_error,
            "detalle": str(e)
        }, 500