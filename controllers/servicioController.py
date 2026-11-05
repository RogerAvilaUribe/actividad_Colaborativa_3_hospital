from models.cita import cita
from models.examen import examen
from models.medicamento import medicamento

class servicioController:
    def __init__(self):
        self.servicios = []

    def agregar_servicioCita(self, tipoServicio, valorServicio, especialidadCita, fechaCita):
        nuevo_servicio = cita(tipoServicio, valorServicio, especialidadCita, fechaCita)
        self.servicios.append(nuevo_servicio)
        print("Servicio agregado exitosamente.")
        return nuevo_servicio

    def agregar_servicioExamen(self, tipoServicio, valorServicio, nombreExamen, fechaExamen):
        nuevo_servicio = examen(tipoServicio, valorServicio, nombreExamen, fechaExamen)
        self.servicios.append(nuevo_servicio)
        print("Servicio agregado exitosamente.")
        return nuevo_servicio

    def agregar_servicioMedicamento(self, tipoServicio, valorServicio, nombreMedicamento, dosis, presentacion):
        nuevo_servicio = medicamento(tipoServicio, valorServicio, nombreMedicamento, dosis, presentacion)
        self.servicios.append(nuevo_servicio)
        print("Servicio agregado exitosamente.")
        return nuevo_servicio

    def get_servicios(self):
        return self.servicios.copy()

    def eliminar_servicio(self, tipoServicio):
        servicio_encontrado = self.buscar_servicio(tipoServicio)
        if servicio_encontrado:
            self.servicios.remove(servicio_encontrado)
            print("Servicio eliminado exitosamente.")
        else:
            print("Servicio no encontrado.")

    # metodo para buscar un servicio por tipo
    def buscar_servicio(self, tipoServicio):
        for servicio in self.servicios:
            if servicio.get_tipoServicio() == tipoServicio:
                return servicio
        return None

    def mostrar_servicios(self):
        if not self.servicios:
            print("No hay servicios registrados.")
            return

        for servicio in self.servicios:
            servicio.mostrar_informacion()
            print("--------------------")
