#Clase: Servicio
from abc import ABC, abstractmethod

class servicio(ABC):
    def __init__(self, tipoServicio, valorServicio):
        self.set_tipoServicio(tipoServicio)
        self.set_valorServicio(valorServicio)

    @abstractmethod
      # otro metodos
    def mostrar_informacion(self):
        print(f"Tipo de servicio: {self.get_tipoServicio()} - Valor del servicio: {self.get_valorServicio()}")
          
    # Setters
    def set_tipoServicio(self, tipoServicio):
        self._tipoServicio = tipoServicio

    def set_valorServicio(self, valorServicio):
        self._valorServicio = valorServicio
    
    # Getters
    def get_tipoServicio(self):
        return self._tipoServicio

    def get_valorServicio(self):
        return self._valorServicio 
    

