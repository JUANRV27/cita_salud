from flask import Blueprint, jsonify, request

from services.usuario_service import (
    obtener_usuarios,
    obtener_usuario_por_id,
    crear_usuario,
    actualizar_usuario,
    eliminar_usuario as eliminar_usuario_service
)

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/", methods=["GET"])
def listar_usuarios():

    return jsonify(obtener_usuarios())

@usuarios_bp.route("/<int:id_usuario>", methods=["GET"])
def obtener_usuario(id_usuario):

    usuario = obtener_usuario_por_id(id_usuario)

    if usuario is None:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    return jsonify(usuario)

@usuarios_bp.route("/", methods=["POST"])
def registrar_usuario():
    datos = request.get_json()

    usuario, codigo = crear_usuario(datos)

    return jsonify(usuario), codigo

@usuarios_bp.route("/<int:id_usuario>", methods=["PUT"])
def editar_usuario(id_usuario):
    datos = request.get_json()

    usuario, codigo = actualizar_usuario(id_usuario, datos)

    return jsonify(usuario), codigo

@usuarios_bp.route("/<int:id_usuario>", methods=["DELETE"])
def borrar_usuario(id_usuario):
    resultado, codigo = eliminar_usuario_service(id_usuario)

    return jsonify(resultado), codigo