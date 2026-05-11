
import logging

# Configuración de Logs 
logging.basicConfig(
    filename='software_fj_logs.txt', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SoftwareFJError(Exception):
    """Clase base para excepciones del sistema Software FJ"""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando los parámetros de la reserva son incorrectos"""
    pass

class ClienteDatosInvalidosError(SoftwareFJError):
    """Se lanza cuando los datos del cliente no pasan la validación"""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio solicitado no existe o no está disponible"""
    pass
