from models.servicio import servicio

class servicioController:
    def __init__(self):
        self.servicios = []
        
    def agregar_servicioCita(self, tipoServicio, valorServicio):
        nuevo_servicio = servicio(tipoServicio, valorServicio)
        self.servicios.append(nuevo_servicio)
        print("Servicio agregado exitosamente.")
    
    def agregar_servicioExamen(self, tipoServicio, valorServicio):
        nuevo_servicio = servicio(tipoServicio, valorServicio)
        self.servicios.append(nuevo_servicio)
        print("Servicio agregado exitosamente.")
    
    def agregar_servicioMedicamento(self, tipoServicio, valorServicio):
        nuevo_servicio = servicio(tipoServicio, valorServicio)
        self.servicios.append(nuevo_servicio)
        print("Servicio agregado exitosamente.")
    
    def eliminar_servicioCita(self, tipoServicio):
        for servicio in self.servicios:
            if servicio.get_tipoServicio() == tipoServicio:
                self.servicios.remove(servicio)
                print("Servicio eliminado exitosamente.")
                return
        print("Servicio no encontrado.")
    
    def eliminar_servicioExamen(self, tipoServicio):
        for servicio in self.servicios:
            if servicio.get_tipoServicio() == tipoServicio:
                self.servicios.remove(servicio)
                print("Servicio eliminado exitosamente.")
                return
        print("Servicio no encontrado.")
    
    def eliminar_servicioMedicamento(self, tipoServicio):
        for servicio in self.servicios:
            if servicio.get_tipoServicio() == tipoServicio:
                self.servicios.remove(servicio)
                print("Servicio eliminado exitosamente.")
                return
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