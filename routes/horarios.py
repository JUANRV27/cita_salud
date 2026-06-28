from flask import Blueprint, request

from services.horario_service import (
    obtener_horarios,
    obtener_horario_por_id,
    crear_horario,
    actualizar_horario,
    eliminar_horario
)

horario_bp = Blueprint(
    "horarios",
    __name__,
    url_prefix="/horarios"
)


@horario_bp.get("/")
def listar_horarios():
    return obtener_horarios()


@horario_bp.get("/<int:id_horario>")
def obtener_horario(id_horario):
    return obtener_horario_por_id(id_horario)


@horario_bp.post("/")
def registrar_horario():
    return crear_horario(request.json)


@horario_bp.put("/<int:id_horario>")
def editar_horario(id_horario):
    return actualizar_horario(
        id_horario,
        request.json
    )


@horario_bp.delete("/<int:id_horario>")
def borrar_horario(id_horario):
    return eliminar_horario(id_horario)