from models.servicio import servicio

#Clase: Examen
class examen(servicio):
    def __init__(self, tipoServicio, valorServicio, nombreExamen):
        super().__init__(tipoServicio, valorServicio)
        self.set_nombreExamen(nombreExamen)
        #self.set_fechaExamen(fechaExamen)

    def mostrar_informacion(self):
        print(f"---INFORMACION EXAMEN---")
        super().mostrar_informacion()
        print(f"Nombre del examen: {self.get_nombreExamen()}")
        #print(f"Fecha del examen: {self.get_fechaExamen()}")

    # Setters
    def set_nombreExamen(self, nombreExamen):
        self._nombreExamen = nombreExamen

    #def set_fechaExamen(self, fechaExamen):
    #    self._fechaExamen = fechaExamen

    # Getters
    def get_nombreExamen(self):
        return self._nombreExamen

    #def get_fechaExamen(self):
    #    return self._fechaExamen
