from flask import Blueprint, request

from services.paciente_service import (
    obtener_pacientes,
    obtener_paciente_por_id,
    crear_paciente,
    actualizar_paciente,
    eliminar_paciente
)

paciente_bp = Blueprint(
    "pacientes",
    __name__,
    url_prefix="/pacientes"
)


@paciente_bp.get("/")
def listar_pacientes():
    return obtener_pacientes()


@paciente_bp.get("/<int:id_paciente>")
def obtener_paciente(id_paciente):
    return obtener_paciente_por_id(id_paciente)


@paciente_bp.post("/")
def registrar_paciente():
    return crear_paciente(request.json)


@paciente_bp.put("/<int:id_paciente>")
def editar_paciente(id_paciente):
    return actualizar_paciente(
        id_paciente,
        request.json
    )


@paciente_bp.delete("/<int:id_paciente>")
def borrar_paciente(id_paciente):
    return eliminar_paciente(id_paciente)