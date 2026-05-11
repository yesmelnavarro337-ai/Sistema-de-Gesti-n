
import logging
from exceptions import *
from models import Cliente
from services import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def procesar_reserva(self, descuento=0):
        try:
            if self.duracion <= 0:
                raise ReservaInvalidaError("La duración debe ser mayor a cero.")
            
            costo = self.servicio.calcular_costo(self.duracion, descuento)
            self.estado = "Confirmada"
            logging.info(f"Reserva exitosa: {self.cliente.get_nombre()} - {self.servicio.nombre_servicio} - Costo: {costo}")
            return costo
        except ReservaInvalidaError as e:
            logging.error(f"Error procesando reserva: {e}")
            self.estado = "Fallida"
            raise
        except Exception as e:
            logging.critical(f"Error inesperado: {e}")
            raise

def ejecutar_simulacion():
    print("--- Iniciando Simulación Software FJ (10 Operaciones) ---")
    servicios = [
        ReservaSalas("S1", "Sala de Juntas", 50000),
        AlquilerEquipos("E1", "Proyector 4K", 30000),
        AsesoriaEspecializada("A1", "Consultoría Software", 120000)
    ]
    
    operaciones = [
        ("VALIDO", "Juan Perez", "juan@mail.com", servicios[0], 3),
        ("VALIDO", "Maria Lopez", "maria@mail.com", servicios[1], 2),
        ("ERROR_CLIENTE", "", "error_mail", servicios[0], 1),
        ("ERROR_RESERVA", "Carlos Ruiz", "carlos@mail.com", servicios[2], -5),
        ("VALIDO", "Ana Gomez", "ana@mail.com", servicios[2], 1),
        ("ERROR_CLIENTE", "L", "l@m.com", servicios[1], 2),
        ("VALIDO", "Luis Torres", "luis@mail.com", servicios[0], 5),
        ("VALIDO", "Elena Mar", "elena@mail.com", servicios[1], 4),
        ("ERROR_RESERVA", "Pedro Pic", "p@mail.com", servicios[0], 0),
        ("VALIDO", "Sofía Sol", "sofia@mail.com", servicios[2], 2),
    ]

    for i, (tipo, nombre, email, servicio, duracion) in enumerate(operaciones, 1):
        print(f"\nOperación {i}: {tipo}")
        try:
            cli = Cliente(f"C{i}", nombre, email)
            res = Reserva(cli, servicio, duracion)
            costo = res.procesar_reserva()
            print(f"Resultado: Éxito. Costo total: {costo}")
        except (ValueError, ClienteDatosInvalidosError) as e:
            print(f"Resultado: Error de validación de cliente -> {e}")
        except ReservaInvalidaError as e:
            print(f"Resultado: Error en reserva -> {e}")
        except Exception as e:
            print(f"Resultado: Error inesperado -> {e}")
        finally:
            # Siempre se ejecuta (Requisito: Bloque finally)
            pass

    print("\n--- Simulación Finalizada. Verifique 'software_fj_logs.txt' ---")

if __name__ == "__main__":
    ejecutar_simulacion()
