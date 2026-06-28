from flask import Blueprint, request

from services.sede_service import (
    obtener_sedes,
    obtener_sede_por_id,
    crear_sede,
    actualizar_sede,
    eliminar_sede
)

sede_bp = Blueprint("sedes", __name__)


@sede_bp.route("/", methods=["GET"])
def listar():
    return obtener_sedes()


@sede_bp.route("/<int:id_sede>", methods=["GET"])
def obtener(id_sede):
    return obtener_sede_por_id(id_sede)


@sede_bp.route("/", methods=["POST"])
def crear():
    return crear_sede(request.json)


@sede_bp.route("/<int:id_sede>", methods=["PUT"])
def actualizar(id_sede):
    return actualizar_sede(id_sede, request.json)


@sede_bp.route("/<int:id_sede>", methods=["DELETE"])
def eliminar(id_sede):
    return eliminar_sede(id_sede)