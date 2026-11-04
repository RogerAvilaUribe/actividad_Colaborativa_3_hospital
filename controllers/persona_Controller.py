from models.administrativo import administrativo
from models.personalSalud import personalSalud
from models.paciente import paciente

class personaController():
    
    def __init__(self):
        self.personas = []

    def agregar_adminitrativo(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, codigoAdministrativo, dependencia, cargo, turno):
        admin = administrativo(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, codigoAdministrativo, dependencia, cargo, turno)
        self.personas.append(admin)
        return admin
    
    def agregar_personalSalud(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, codigoPersonalSalud, registroProfesional, dependencia, codigoEspecialidad, numeroDeHorasSemanales, turno):
        persalud = personalSalud(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, codigoPersonalSalud, registroProfesional, dependencia, codigoEspecialidad, numeroDeHorasSemanales, turno)
        self.personas.append(persalud)
        return persalud
    
    def agregar_paciente(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, codigoPaciente, fechaNacimiento, genero, tipoSangre):
        paci = paciente(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, codigoPaciente, fechaNacimiento, genero, tipoSangre)
        self.personas.append(paci)
        return paci
    
    def get_personas(self):
        return self.personas.copy()
    