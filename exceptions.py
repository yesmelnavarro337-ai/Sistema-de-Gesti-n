import logging

# --- CONFIGURACIÓN DE PERSISTENCIA DE ERRORES ---
# Se utiliza el módulo logging para cumplir con el requisito de registro de eventos en archivos
# El archivo 'SistemaGestion.txt' almacenará la trazabilidad de errores sin detener la aplicación
logging.basicConfig(
    filename='SistemaGestion.txt', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- JERARQUÍA DE EXCEPCIONES PERSONALIZADAS ---
# Requisito: Uso de excepciones personalizadas para un manejo profesional del sistema

class SoftwareFJError(Exception):
    """
    Clase base (Superclase) para todas las excepciones del sistema
    Hereda de la clase base Exception de Python para integrar la lógica de errores propia
    """
    pass

class ReservaInvalidaError(SoftwareFJError):
    """
    Excepción lanzada ante intentos de reserva incorrectos o parámetros fuera de rango
    Ejemplo: Duraciones menores o iguales a cero.
    """
    pass

class ClienteDatosInvalidosError(SoftwareFJError):
    """
    Se dispara cuando los datos personales del cliente no cumplen con las validaciones 
    estrictas de la clase Cliente (Encapsulación)
    """
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """
    Gestiona situaciones donde se intenta acceder a un servicio que no existe o 
    cuya operación no está permitida en el momento
    """
    pass
