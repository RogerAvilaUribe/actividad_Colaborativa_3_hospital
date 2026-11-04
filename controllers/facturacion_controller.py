from models.facturacion import facturacion

class facturacionController():

    def __init__(self):
        self.facturas = []

    def agregar_factura(self, codigoFactura, paciente, servicio, personalSalud, administrativo, fechaFactura, total):
        factura = facturacion(codigoFactura, paciente, servicio, personalSalud, administrativo, fechaFactura, total)
        self.facturas.append(factura)

    def eliminar_factura(self, codigoFactura):
        for factura in self.facturas:
            if factura.get_codigoFactura() == codigoFactura:
                self.facturas.remove(factura)
                return True
        return False

    def mostrar_facturas(self):
        for factura in self.facturas:
            factura.mostrar_informacion()
            print("--------------------")

    def buscar_factura(self, codigoFactura):
        for factura in self.facturas:
            if factura.get_codigoFactura() == codigoFactura:
                return factura
        return None
    