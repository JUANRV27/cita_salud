from models.rol import Rol


def obtener_roles():
    roles = Rol.query.all()

    return [rol.to_dict() for rol in roles]


def obtener_rol_por_id(id_rol):
    rol = Rol.query.get(id_rol)

    if rol is None:
        return None

    return rol.to_dict()