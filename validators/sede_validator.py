from models.sede import Sede


def validar_nombre_unico(nombre):

    sede = Sede.query.filter_by(
        nombre_sede=nombre
    ).first()

    if sede:
        return {
            "error": "La sede ya existe."
        }, 409

    return None


def validar_nombre_actualizacion(id_sede, nombre):

    sede = Sede.query.filter_by(
        nombre_sede=nombre
    ).first()

    if sede and sede.id_sede != id_sede:
        return {
            "error": "La sede ya existe."
        }, 409

    return None