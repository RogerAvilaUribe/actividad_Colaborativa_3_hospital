from models.persona import persona

class administrativo (persona):

    def __init__(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, dependencia, cargo, turno):
        super().__init__(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso)
        self.setDependencia(dependencia)
        self.setCargo(cargo)
        self.setTurno(turno)

    def mostrar_informacion(self):
        print(f"---INFORMACION DEL COLABORADOR ADMINISTRATIVO---")
        super().mostrar_informacion()
        print(f"Dependencia: {self.getDependencia()}")
        print(f"Cargo: {self.getCargo()}")
        print(f"Turno: {self.getTurno()}")

    def realizar_actividad_principal(self):
        print(f"El colaborador administrativo {self.get_nombre()} se encuentra trabajando en la dependencia de {self.getDependencia()} y tiene el cargo de {self.getCargo()}.")

    # SETTERS
    def setDependencia(self, dependencia):
        self._dependencia = dependencia

    def setCargo(self, cargo):
        self._cargo = cargo

    def setTurno(self, turno):
        self._turno = turno

    # GETTERS
    def getDependencia(self):
        return self._dependencia

    def getCargo(self):
        return self._cargo

    def getTurno(self):
        return self._turno
