from flask import Blueprint, request

from services.medico_service import (
    obtener_medicos,
    obtener_medico_por_id,
    crear_medico,
    actualizar_medico,
    eliminar_medico
)

medico_bp = Blueprint(
    "medicos",
    __name__,
    url_prefix="/medicos"
)


@medico_bp.get("/")
def listar_medicos():
    return obtener_medicos()


@medico_bp.get("/<int:id_medico>")
def obtener_medico(id_medico):
    return obtener_medico_por_id(id_medico)


@medico_bp.post("/")
def registrar_medico():
    return crear_medico(request.json)


@medico_bp.put("/<int:id_medico>")
def editar_medico(id_medico):
    return actualizar_medico(
        id_medico,
        request.json
    )


@medico_bp.delete("/<int:id_medico>")
def borrar_medico(id_medico):
    return eliminar_medico(id_medico)