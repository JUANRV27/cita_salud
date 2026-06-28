from flask import Blueprint, request

from services.cita_service import (
    obtener_citas,
    obtener_cita_por_id,
    crear_cita,
    actualizar_cita,
    cancelar_cita,
    eliminar_cita
)

cita_bp = Blueprint(
    "citas",
    __name__,
    url_prefix="/citas"
)


@cita_bp.get("/")
def listar_citas():
    return obtener_citas()


@cita_bp.get("/<int:id_cita>")
def obtener_cita(id_cita):
    return obtener_cita_por_id(id_cita)


@cita_bp.post("/")
def registrar_cita():
    return crear_cita(request.json)


@cita_bp.put("/<int:id_cita>")
def editar_cita(id_cita):
    return actualizar_cita(
        id_cita,
        request.json
    )


@cita_bp.put("/<int:id_cita>/cancelar")
def cancelar(id_cita):
    return cancelar_cita(id_cita)


@cita_bp.delete("/<int:id_cita>")
def borrar_cita(id_cita):
    return eliminar_cita(id_cita)