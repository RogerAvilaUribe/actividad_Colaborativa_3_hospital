from models.servicio import servicio

#Clase: Medicamento
class medicamento(servicio):
    def __init__(self, tipoServicio, valorServicio, nombreMedicamento, dosis, presentacion):
        super().__init__(tipoServicio, valorServicio)
        self.set_nombreMedicamento(nombreMedicamento)
        self.set_dosis(dosis)
        self.set_presentacion(presentacion)

    def mostrar_informacion(self):
        print(f"---INFORMACION MEDICAMENTO---")
        super().mostrar_informacion()
        print(f"Nombre del medicamento: {self.get_nombreMedicamento()}")
        print(f"Dosis: {self.get_dosis()}")
        print(f"Presentacion: {self.get_presentacion()}")

    # Setters
    def set_nombreMedicamento(self, nombreMedicamento):
        self._nombreMedicamento = nombreMedicamento

    def set_dosis(self, dosis):
        self._dosis = dosis

    def set_presentacion(self, presentacion):
        self._presentacion = presentacion

    # Getters
    def get_nombreMedicamento(self):
        return self._nombreMedicamento

    def get_dosis(self):
        return self._dosis

    def get_presentacion(self):
        return self._presentacion
