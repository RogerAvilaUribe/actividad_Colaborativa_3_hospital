class FechaNacimientoInvalida(Exception):
    """ El paciente no puede tener una fecha de nacimiento futura ni vacía. """
    
    def __init__(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento
        super().__init__(
            f"La fecha de nacimiento '{self.fechaNacimiento}' es inválida. Debe ser una fecha pasada y no vacía."
        )
        
        
class IdentificacionNoPuedeEstarVacia(Exception):
    """ La identificación del usuario no puede estar vacía. """
    
    def __init__(self, identificacion):
        self.identificacion = identificacion
        super().__init__(
            f"La identificación '{self.identificacion}' es inválida. No puede estar vacía."
        )


class ServicioObligatorioAlFacturar(Exception):
    """ No se puede facturar un servicio sin haberlo prestado. """
    
    def __init__(self, servicio):
        self.servicio = servicio
        super().__init__(
            f"El servicio '{self.servicio}' no ha sido prestado. No se puede facturar un servicio que no ha sido prestado."
        )

class CodigoFacturaInvalido(Exception):
    """ El código de la factura no puede estar vacío. """
    
    def __init__(self, codigoFactura):
        self.codigoFactura = codigoFactura
        super().__init__(
            f"El código de la factura '{self.codigoFactura}' es inválido. No puede estar vacío."
        )
        