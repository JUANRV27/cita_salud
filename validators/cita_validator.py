from models.paciente import Paciente
from models.horario_disponible import HorarioDisponible
from models.cita import Cita


def validar_paciente(id_paciente):
    if Paciente.query.get(id_paciente) is None:
        return {"error": "El paciente no existe."}, 404
    return None


def validar_horario(id_horario):
    if HorarioDisponible.query.get(id_horario) is None:
        return {"error": "El horario no existe."}, 404
    return None


def validar_horario_disponible(id_horario):
    horario = HorarioDisponible.query.get(id_horario)

    if horario and not horario.estado_disponible:
        return {"error": "El horario no está disponible."}, 400

    return None


def validar_horario_sin_cita(id_horario):
    cita = Cita.query.filter_by(id_horario=id_horario).first()

    if cita:
        return {"error": "Ya existe una cita para este horario."}, 409

    return None