from flask import Blueprint, jsonify, request

from services.especialidad_service import (
    obtener_especialidades,
    obtener_especialidad_por_id,
    crear_especialidad,
    actualizar_especialidad,
    eliminar_especialidad
)

especialidades_bp = Blueprint("especialidades", __name__)


@especialidades_bp.route("/", methods=["GET"])
def listar_especialidades():
    return jsonify(obtener_especialidades())


@especialidades_bp.route("/<int:id_especialidad>", methods=["GET"])
def obtener_especialidad(id_especialidad):
    resultado, codigo = obtener_especialidad_por_id(id_especialidad)
    return jsonify(resultado), codigo


@especialidades_bp.route("/", methods=["POST"])
def registrar_especialidad():
    resultado, codigo = crear_especialidad(request.json)
    return jsonify(resultado), codigo


@especialidades_bp.route("/<int:id_especialidad>", methods=["PUT"])
def editar_especialidad(id_especialidad):
    resultado, codigo = actualizar_especialidad(id_especialidad, request.json)
    return jsonify(resultado), codigo


@especialidades_bp.route("/<int:id_especialidad>", methods=["DELETE"])
def borrar_especialidad(id_especialidad):
    resultado, codigo = eliminar_especialidad(id_especialidad)
    return jsonify(resultado), codigo