
from abc import ABC, abstractmethod

# --- CLASE ABSTRACTA SERVICIO ---
# Requisito: Una clase abstracta Servicio que defina la estructura para los servicios especializados
class Servicio(ABC):
    """
    Define la interfaz común para todos los servicios de Software FJ.
    La abstracción asegura que no se puedan crear servicios genéricos, 
    obligando a definir tipos específicos (Salas, Equipos, Asesorías)
    """
    def __init__(self, id_servicio, nombre_servicio, precio_base):
        # Atributos públicos que comparten todos los servicios por herencia
        self.id_servicio = id_servicio
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        """
        Método abstracto para el cálculo de costos. 
        Obliga a las clases derivadas a implementar su propia lógica (Polimorfismo).
        
        Parámetros:
        - duracion: cantidad de tiempo/unidades del servicio.
        - descuento: parámetro opcional que demuestra la sobrecarga de métodos mediante 
          valores por defecto.
        """
        pass

    def __str__(self):
        """
        Método especial para representar el objeto como una cadena de texto.
        """
        return f"Servicio: {self.nombre_servicio} (ID: {self.id_servicio})"

# --- CLASES DERIVADAS (IMPLEMENTACIÓN DE POLIMORFISMO) ---
# Requisito: Al menos tres servicios especializados que hereden de la clase abstracta

class ReservaSalas(Servicio):
    """
    Servicio especializado en reserva de espacios físicos.
    Implementa el cálculo de costo basado en horas de uso
    """
    def calcular_costo(self, horas, descuento=0):
        # Sobrescribe el método base aplicando una lógica de cobro por hora 
        total = (self.precio_base * horas) - descuento
        return max(total, 0)

class AlquilerEquipos(Servicio):
    """
    Servicio especializado en préstamo de herramientas tecnológicas.
    Implementa el cálculo de costo basado en días de alquiler
    """
    def calcular_costo(self, dias, descuento=0):
        # Sobrescribe el método base aplicando una lógica de cobro por día 
        total = (self.precio_base * dias) - descuento
        return max(total, 0)

class AsesoriaEspecializada(Servicio):
    """
    Servicio de consultoría técnica.
    Implementa el cálculo de costo por sesiones e incluye un recargo administrativo
    """
    def calcular_costo(self, sesiones, descuento=0):
        # Demuestra polimorfismo al incluir un 'recargo' único para este tipo de servicio 
        recargo = 5000 
        total = (self.precio_base * sesiones + recargo) - descuento
        return max(total, 0)
