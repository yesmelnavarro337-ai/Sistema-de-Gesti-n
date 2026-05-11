import logging
# Importación de módulos locales que contienen la lógica de excepciones, modelos y servicios
from exceptions import *
from models import Cliente
from services import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada

# --- CLASE DE NEGOCIO: RESERVA ---
# Esta clase actúa como integradora entre el Cliente y el Servicio solicitado (Agregación) 
class Reserva:
    """
    Clase que gestiona la relación entre un cliente, un servicio y la duración.
    Implementa la lógica de procesamiento con manejo de excepciones.
    """
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def procesar_reserva(self, descuento=0):
        """
        Calcula el costo total usando polimorfismo y gestiona posibles errores de parámetros.
        """
        try:
            # Validación de regla de negocio: la duración no puede ser negativa o cero 
            if self.duracion <= 0:
                # Se lanza una excepción personalizada si la validación falla 
                raise ReservaInvalidaError("La duración debe ser mayor a cero.")
            
            # POLIMORFISMO: Se llama a calcular_costo() sin importar el tipo de servicio específico 
            costo = self.servicio.calcular_costo(self.duracion, descuento)
            self.estado = "Confirmada"
            
            # REGISTRO DE EVENTOS (Logs): Se guarda el éxito de la operación en el archivo externo 
            logging.info(f"Reserva exitosa: {self.cliente.get_nombre()} - {self.servicio.nombre_servicio} - Costo: {costo}")
            return costo
            
        except ReservaInvalidaError as e:
            # Manejo específico para errores de reserva, registrando el fallo en el log 
            logging.error(f"Error procesando reserva: {e}")
            self.estado = "Fallida"
            raise # Re-lanza la excepción para que sea capturada en el ciclo de simulación
            
        except Exception as e:
            # Captura cualquier error no previsto para mantener la estabilidad del sistema
            logging.critical(f"Error inesperado: {e}")
            raise

# --- MOTOR DE SIMULACIÓN ---
def ejecutar_simulacion():
    """
    Simula 10 operaciones (éxitos y fallos) para demostrar la robustez del sistema
    """
    print("--- Iniciando Simulacion Sistema Gestion (10 Operaciones) ---")
    
    # Creación de servicios disponibles utilizando las clases derivadas 
    servicios = [
        ReservaSalas("S1", "Sala de Juntas", 50000),
        AlquilerEquipos("E1", "Proyector 4K", 30000),
        AsesoriaEspecializada("A1", "Consultoría Software", 120000)
    ]
    
    # Matriz de datos para simular registros válidos e inválidos 
    operaciones = [
        ("VALIDO", "Juan Perez", "juan@mail.com", servicios[0], 3),
        ("VALIDO", "Maria Lopez", "maria@mail.com", servicios[1], 2),
        ("ERROR_CLIENTE", "", "error_mail", servicios[0], 1), # Nombre vacío disparará ValueError
        ("ERROR_RESERVA", "Carlos Ruiz", "carlos@mail.com", servicios[2], -5), # Duración negativa
        ("VALIDO", "Ana Gomez", "ana@mail.com", servicios[2], 1),
        ("ERROR_CLIENTE", "L", "l@m.com", servicios[1], 2), # Nombre muy corto
        ("VALIDO", "Luis Torres", "luis@mail.com", servicios[0], 5),
        ("VALIDO", "Elena Mar", "elena@mail.com", servicios[1], 4),
        ("ERROR_RESERVA", "Pedro Pic", "p@mail.com", servicios[0], 0), # Duración cero
        ("VALIDO", "Sofía Sol", "sofia@mail.com", servicios[2], 2),
    ]

    # Iteración sobre las operaciones simuladas
    for i, (tipo, nombre, email, servicio, duracion) in enumerate(operaciones, 1):
        print(f"\nOperación {i}: {tipo}")
        try:
            # BLOQUE TRY: Intento de instanciación y procesamiento 
            cli = Cliente(f"C{i}", nombre, email) # Valida datos del cliente (Encapsulación) 
            res = Reserva(cli, servicio, duracion)
            costo = res.procesar_reserva()
            print(f"Resultado: Éxito. Costo total: {costo}")
            
        except (ValueError, ClienteDatosInvalidosError) as e:
            # Captura errores de validación de datos personales del cliente 
            print(f"Resultado: Error de validación de cliente -> {e}")
            
        except ReservaInvalidaError as e:
            # Captura errores específicos de la lógica de negocio de reservas 
            print(f"Resultado: Error en reserva -> {e}")
            
        except Exception as e:
            # Captura errores genéricos para asegurar que el programa NO se detenga 
            print(f"Resultado: Error inesperado -> {e}")
            
        finally:
            # BLOQUE FINALLY: Se ejecuta siempre, garantizando la continuidad del ciclo 
            pass

    print("\n--- Simulación Finalizada. Verifique el archivo de logs ---")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    ejecutar_simulacion()
