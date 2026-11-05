from models.servicio import servicio

#Clase: Cita
class cita(servicio):
    def __init__(self, tipoServicio, valorServicio, especialidadCita, fechaCita):
        super().__init__(tipoServicio, valorServicio)
        self.set_especialidadCita(especialidadCita)
        self.set_fechaCita(fechaCita)

    def mostrar_informacion(self):
        print(f"---INFORMACION CITA---")
        super().mostrar_informacion()
        print(f"Especialidad de la cita: {self.get_especialidadCita()}")
        print(f"Fecha de la cita: {self.get_fechaCita()}")

    # Setters
    def set_especialidadCita(self, especialidadCita):
        self._especialidadCita = especialidadCita

    def set_fechaCita(self, fechaCita):
        self._fechaCita = fechaCita

    # Getters
    def get_especialidadCita(self):
        return self._especialidadCita

    def get_fechaCita(self):
        return self._fechaCita
