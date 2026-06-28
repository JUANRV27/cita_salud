from database import db
from models.especialidad import Especialidad

from validators.common import (
    validar_campos_requeridos,
    ejecutar_validaciones
)
from validators.especialidad_validator import (
    validar_nombre_unico,
    validar_nombre_actualizacion
)

CAMPOS_REQUERIDOS = [
    "nombre_especialidad"
]

def obtener_especialidades():
    especialidades = Especialidad.query.all()

    return [especialidad.to_dict() for especialidad in especialidades]

def obtener_especialidad_por_id(id_especialidad):
    especialidad = Especialidad.query.get(id_especialidad)

    if especialidad is None:
        return {
            "error": "Especialidad no encontrada."
        }, 404

    return especialidad.to_dict(), 200

def crear_especialidad(datos):
    
    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(datos, CAMPOS_REQUERIDOS),
        lambda: validar_nombre_unico(datos["nombre_especialidad"])
    ])

    if error:
        return error

    try:
        especialidad = Especialidad(
            nombre_especialidad=datos["nombre_especialidad"]
        )

        db.session.add(especialidad)
        db.session.commit()

    except Exception:
        db.session.rollback()

        return {
            "error": "No fue posible crear la especialidad."
        }, 500

    return especialidad.to_dict(), 201

def actualizar_especialidad(id_especialidad, datos):
    especialidad = Especialidad.query.get(id_especialidad)

    if especialidad is None:
        return {
            "error": "Especialidad no encontrada."
        }, 404

    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(datos, CAMPOS_REQUERIDOS),
        lambda: validar_nombre_actualizacion(id_especialidad, datos["nombre_especialidad"])
    ])

    if error:
        return error

    try:
        especialidad.nombre_especialidad = datos["nombre_especialidad"]
        db.session.commit()

    except Exception:
        db.session.rollback()

        return {
            "error": "No fue posible actualizar la especialidad."
        }, 500

    return especialidad.to_dict(), 200

def eliminar_especialidad(id_especialidad):
    especialidad = Especialidad.query.get(id_especialidad)

    if especialidad is None:
        return {
            "error": "Especialidad no encontrada."
        }, 404

    try:
        db.session.delete(especialidad)
        db.session.commit()

    except Exception:
        db.session.rollback()

        return {
            "error": "No fue posible eliminar la especialidad."
        }, 500

    return {
        "mensaje": "Especialidad eliminada correctamente."
    }, 200