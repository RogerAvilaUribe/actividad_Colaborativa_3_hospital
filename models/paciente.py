from models.persona import persona

class paciente (persona):

    def __init__(self, nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, fechaNacimiento, contactoEmergencia, nombreEps):
        super().__init__(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso)
        self.setFechaNacimiento(fechaNacimiento)
        self.setContactoEmergencia(contactoEmergencia)
        self.setNombreEps(nombreEps)

    def mostrar_informacion(self):
        print(f"---INFORMACION PACIENTE---")
        super().mostrar_informacion()
        print(f"Codigo del paciente: {self.getCodigoPaciente()}")
        print(f"Fecha de nacimiento: {self.getFechaNacimiento()}")
        print(f"Contacto de emergencia: {self.getContactoEmergencia()}")
        print(f"Eps a la que pertenece: {self.getNombreEps()}")

    def realizar_actividad_principal(self):
        print(f"El paciente {self.get_nombre()} se encuentra afiliado a {self.getNombreEps()}.")

    # SETTERS
    def setFechaNacimiento(self, fechaNacimiento):
        self._fechaNacimiento = fechaNacimiento 

    def setContactoEmergencia(self, contactoEmergencia):
        self._contactoEmergencia = contactoEmergencia

    def setNombreEps(self, nombreEps):
        self._nombreEps = nombreEps

    # GETTERS
    def getFechaNacimiento(self):
        return self._fechaNacimiento

    def getContactoEmergencia(self):
        return self._contactoEmergencia

    def getNombreEps(self):
        return self._nombreEps