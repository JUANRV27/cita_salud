from database import db
from models.sede import Sede

from validators.common import (
    validar_campos_requeridos,
    ejecutar_validaciones
)

from validators.sede_validator import (
    validar_nombre_unico,
    validar_nombre_actualizacion
)

CAMPOS_REQUERIDOS = [
    "nombre_sede",
    "direccion"
]


def obtener_sedes():

    sedes = Sede.query.all()

    return [sede.to_dict() for sede in sedes]


def obtener_sede_por_id(id_sede):

    sede = Sede.query.get(id_sede)

    if sede is None:
        return {
            "error": "Sede no encontrada."
        }, 404

    return sede.to_dict(), 200


def crear_sede(datos):

    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(
            datos,
            CAMPOS_REQUERIDOS
        ),
        lambda: validar_nombre_unico(
            datos["nombre_sede"]
        )
    ])

    if error:
        return error

    try:

        sede = Sede(
            nombre_sede=datos["nombre_sede"],
            direccion=datos["direccion"]
        )

        db.session.add(sede)
        db.session.commit()

    except Exception:

        db.session.rollback()

        return {
            "error": "No fue posible crear la sede."
        }, 500

    return sede.to_dict(), 201


def actualizar_sede(id_sede, datos):

    sede = Sede.query.get(id_sede)

    if sede is None:
        return {
            "error": "Sede no encontrada."
        }, 404

    error = ejecutar_validaciones([
        lambda: validar_campos_requeridos(
            datos,
            CAMPOS_REQUERIDOS
        ),
        lambda: validar_nombre_actualizacion(
            id_sede,
            datos["nombre_sede"]
        )
    ])

    if error:
        return error

    try:

        sede.nombre_sede = datos["nombre_sede"]
        sede.direccion = datos["direccion"]

        db.session.commit()

    except Exception:

        db.session.rollback()

        return {
            "error": "No fue posible actualizar la sede."
        }, 500

    return sede.to_dict(), 200


def eliminar_sede(id_sede):

    sede = Sede.query.get(id_sede)

    if sede is None:
        return {
            "error": "Sede no encontrada."
        }, 404

    try:

        db.session.delete(sede)
        db.session.commit()

    except Exception:

        db.session.rollback()

        return {
            "error": "No fue posible eliminar la sede."
        }, 500

    return {
        "mensaje": "Sede eliminada correctamente."
    }, 200