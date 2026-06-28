import re


def validar_campos_requeridos(datos, campos):
    """
    Verifica que todos los campos requeridos existan en el payload.
    """

    for campo in campos:
        if campo not in datos:
            return {
                "error": f"El campo '{campo}' es obligatorio."
            }, 400

    return None

def validar_campos_requeridos(datos, campos):
    for campo in campos:
        if campo not in datos:
            return {
                "error": f"El campo '{campo}' es obligatorio."
            }, 400

    return None


def validar_formato_correo(correo):

    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(patron, correo):
        return {
            "error": "El correo electrónico no tiene un formato válido."
        }, 400

    return None


def validar_telefono(telefono):

    if not telefono.isdigit():
        return {
            "error": "El teléfono solo puede contener números."
        }, 400

    if len(telefono) != 9:
        return {
            "error": "El teléfono debe tener exactamente 9 dígitos."
        }, 400

    return None


def validar_password(password):

    if len(password) < 6:
        return {
            "error": "La contraseña debe tener al menos 6 caracteres."
        }, 400

    return None

def ejecutar_validaciones(validaciones):
    """
    Ejecuta una lista de funciones de validación.

    Cada elemento de la lista debe ser una función sin argumentos
    (por ejemplo, usando lambda) que retorne:
    - None si la validación es correcta.
    - (respuesta, código) si falla.
    """

    for validacion in validaciones:
        resultado = validacion()

        if resultado is not None:
            return resultado

    return None