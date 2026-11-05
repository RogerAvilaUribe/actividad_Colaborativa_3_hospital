from models.administrativo import administrativo
from models.personalSalud import personalSalud
from models.paciente import paciente

class personaController():
    
    def __init__(self):
        self.personas = []

    def agregar_adminitrativo(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, dependencia, cargo, turno):
        admin = administrativo(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, dependencia, cargo, turno)
        self.personas.append(admin)
        return admin
    
    def agregar_personalSalud(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, registroProfesional, dependencia, codigoEspecialidad, numeroDeHorasSemanales, turno):
        persalud = personalSalud(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, registroProfesional, dependencia, codigoEspecialidad, numeroDeHorasSemanales, turno)
        self.personas.append(persalud)
        return persalud
    
    def agregar_paciente(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, fechaNacimiento, contactoEmergencia, nombreEps):
        paci = paciente(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, fechaNacimiento, contactoEmergencia, nombreEps)
        self.personas.append(paci)
        return paci
    
    def get_personas(self):
        return self.personas.copy()
    
    def eliminar_paciente(self, identificacion):
        for paciente in self.personas:
            if paciente.get_identificacion() == identificacion:
                self.personas.remove(paciente)
                return True
        return False
    
    def eliminar_personalSalud(self, identificacion):
            for personalSalud in self.personas:
                if personalSalud.get_identificacion() == identificacion:
                    self.personas.remove(personalSalud)
                    return True
            return False
        
    def eliminar_administrativo(self, identificacion):
        for administrativo in self.personas:
            if administrativo.get_identificacion() == identificacion:
                self.personas.remove(administrativo)
                return True
        return False
    