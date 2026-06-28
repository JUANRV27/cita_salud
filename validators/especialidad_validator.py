from models.especialidad import Especialidad


def validar_nombre_unico(nombre):

    especialidad = Especialidad.query.filter_by(
        nombre_especialidad=nombre
    ).first()

    if especialidad:
        return {
            "error": "La especialidad ya existe."
        }, 409

    return None


def validar_nombre_actualizacion(id_especialidad, nombre):

    especialidad = Especialidad.query.filter_by(
        nombre_especialidad=nombre
    ).first()

    if (
        especialidad
        and especialidad.id_especialidad != id_especialidad
    ):
        return {
            "error": "La especialidad ya existe."
        }, 409

    return None