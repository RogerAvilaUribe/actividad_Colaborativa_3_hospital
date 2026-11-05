class FechaNacimientoInvalida(Exception):
    """ El paciente no puede tener una fecha de nacimiento futura ni vacía. """
    
    def __init__(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento
        super().__init__(
            f"La fecha de nacimiento '{self.fechaNacimiento}' es inválida. Debe ser una fecha pasada y no vacía."
        )
        
        
class CitasElMismoDia(Exception):
    """ No se puede agendar una cita para el mismo paciente en la misma fecha. """
    
    def __init__(self, fechaCita):
        self.fechaCita = fechaCita
        super().__init__(
            f"Ya existe una cita agendada para la fecha '{self.fechaCita}'. No se puede agendar otra cita para el mismo paciente en la misma fecha."
        )


class ServicioObligatorioAlFacturar(Exception):
    """ No se puede facturar un servicio sin haberlo prestado. """
    
    def __init__(self, servicio):
        self.servicio = servicio
        super().__init__(
            f"El servicio '{self.servicio}' no ha sido prestado. No se puede facturar un servicio que no ha sido prestado."
        )
        