from models.persona import persona

class personalSalud (persona):

    def __init__(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, registroProfesional, dependencia, especialidad, numeroDeHorasSemanales, turno):
        super().__init__(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso)
        self.setRegistroProfesional(registroProfesional)
        self.setDependencia(dependencia)
        self.setEspecialidad(especialidad)
        self.setNumeroDeHorasSemanales(numeroDeHorasSemanales)
        self.setTurno(turno)

    def mostrar_informacion(self):
        print(f"---INFORMACION DEL COLABORAADOR PERSONAL DE LA SALUD---")
        super().mostrar_informacion()
        print(f"Registro profesional: {self.getRegistroProfesional()}")
        print(f"Dependencia: {self.getDependencia()}")
        print(f"Codigo especialidad: {self.getEspecialidad()}")
        print(f"Numero de horas semanales: {self.getNumeroDeHorasSemanales()}")
        print(f"turno de trabajo: {self.getTurno()}")

    def realizar_actividad_principal(self):
        print(f"El colaborador {self.get_nombre()} se encuentra en la dependencia de {self.getDependencia()}.")

    # SETTERS
    def setRegistroProfesional(self, registroProfesional):
        self._registroProfesional = registroProfesional 

    def setDependencia(self, dependencia):
        self._dependencia = dependencia

    def setEspecialidad(self, codigoEspecialidad):
        self._codigoEspecialidad = codigoEspecialidad

    def setNumeroDeHorasSemanales(self, numeroDeHorasSemanales):
        self._numeroDeHorasSemanales = numeroDeHorasSemanales

    def setTurno(self, turno):
        self._turno = turno

    # GETTERS
    def getRegistroProfesional(self):
        return self._registroProfesional

    def getDependencia(self):
        return self._dependencia

    def getEspecialidad(self):
        return self._codigoEspecialidad

    def getNumeroDeHorasSemanales(self):
        return self._numeroDeHorasSemanales

    def getTurno(self):
        return self._turno