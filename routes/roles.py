from flask import Blueprint, jsonify

from services.rol_service import (
    obtener_roles,
    obtener_rol_por_id
)

roles_bp = Blueprint("roles", __name__)


@roles_bp.route("/", methods=["GET"])
def listar_roles():

    return jsonify(obtener_roles())


@roles_bp.route("/<int:id_rol>", methods=["GET"])
def obtener_rol(id_rol):

    rol = obtener_rol_por_id(id_rol)

    if rol is None:
        return jsonify({
            "error": "Rol no encontrado"
        }), 404

    return jsonify(rol)