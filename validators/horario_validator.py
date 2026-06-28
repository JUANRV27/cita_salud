from models.medico import Medico
from models.sede import Sede
from models.horario_disponible import HorarioDisponible


def validar_medico(id_medico):

    if Medico.query.get(id_medico) is None:
        return {
            "error": "El médico no existe."
        }, 404

    return None


def validar_sede(id_sede):

    if Sede.query.get(id_sede) is None:
        return {
            "error": "La sede no existe."
        }, 404

    return None


def validar_horas(hora_inicio, hora_fin):

    if hora_inicio >= hora_fin:
        return {
            "error": "La hora de inicio debe ser menor que la hora de fin."
        }, 400

    return None


def validar_horario_repetido(
    id_medico,
    fecha,
    hora_inicio
):

    horario = HorarioDisponible.query.filter_by(
        id_medico=id_medico,
        fecha=fecha,
        hora_inicio=hora_inicio
    ).first()

    if horario:
        return {
            "error": "Ya existe un horario para ese médico."
        }, 409

    return None