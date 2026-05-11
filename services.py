
from abc import ABC, abstractmethod

# Clase Abstracta Servicio (Requisito: Clase abstracta Servicio)
class Servicio(ABC):
    def __init__(self, id_servicio, nombre_servicio, precio_base):
        self.id_servicio = id_servicio
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        # Requisito: Polimorfismo y métodos sobrescritos
        pass

    def __str__(self):
        return f"Servicio: {self.nombre_servicio} (ID: {self.id_servicio})"

# Derivada 1: Reservas de Salas
class ReservaSalas(Servicio):
    def calcular_costo(self, horas, descuento=0):
        total = (self.precio_base * horas) - descuento
        return max(total, 0)

# Derivada 2: Alquiler de Equipos
class AlquilerEquipos(Servicio):
    def calcular_costo(self, dias, descuento=0):
        total = (self.precio_base * dias) - descuento
        return max(total, 0)

# Derivada 3: Asesorías Especializadas
class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones, descuento=0):
        recargo = 5000 
        total = (self.precio_base * sesiones + recargo) - descuento
        return max(total, 0)
