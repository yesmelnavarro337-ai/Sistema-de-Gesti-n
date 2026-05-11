
from abc import ABC, abstractmethod
import logging

# --- CLASE ABSTRACTA GENERAL ---
# Requisito: Una clase abstracta que represente entidades generales del sistema
class EntidadBase(ABC):
    """
    Define la estructura base para todas las entidades del sistema.
    Utiliza la clase ABC (Abstract Base Classes) para impedir la instanciación directa
    y obligar a las clases derivadas a implementar métodos específicos.
    """
    def __init__(self, id_entidad):
        # Atributo protegido que identifica de forma única a la entidad
        self.id_entidad = id_entidad

    @abstractmethod
    def obtener_detalles(self):
        """
        Método abstracto que debe ser sobrescrito por las subclases (Polimorfismo).
        """
        pass

# --- CLASE CLIENTE ---
# Requisito: Clase Cliente con validaciones robustas y encapsulación de datos personales
class Cliente(EntidadBase):
    """
    Representa a los clientes de Software FJ. Implementa herencia de EntidadBase
    y asegura que los datos sensibles no sean modificados incorrectamente.
    """
    def __init__(self, id_cliente, nombre, email):
        # Llamada al constructor de la clase padre (Herencia)
        super().__init__(id_cliente)
        
        # Atributos privados (__): Implementación rigurosa de la Encapsulación.
        # No se puede acceder a ellos directamente desde fuera de la clase.
        self.__nombre = None
        self.__email = None
        
        # Uso de setters para aplicar validaciones durante la creación del objeto
        self.set_nombre(nombre)
        self.set_email(email)

    # --- MÉTODOS DE ACCESO (Getters y Setters) ---
    # Estos métodos permiten controlar cómo se leen y escriben los datos personales.

    def set_nombre(self, nombre):
        """
        Validación robusta: Asegura que el nombre no sea nulo y tenga una longitud mínima.
        Si la validación falla, se lanza una excepción de valor (ValueError).
        """
        if not nombre or len(nombre) < 3:
            raise ValueError("Nombre de cliente inválido (mínimo 3 caracteres).")
        self.__nombre = nombre

    def get_nombre(self):
        """
        Permite obtener el nombre de forma controlada.
        """
        return self.__nombre

    def set_email(self, email):
        """
        Validación robusta: Verifica que el correo electrónico contenga el símbolo '@'.
        """
        if "@" not in email:
            raise ValueError("Formato de email incorrecto.")
        self.__email = email

    # --- IMPLEMENTACIÓN DE MÉTODO ABSTRACTO ---
    def obtener_detalles(self):
        """
        Sobrescribe el método de la clase base para devolver información específica
        del cliente, demostrando el uso de herencia y polimorfismo.
        """
        return f"ID: {self.id_entidad} | Cliente: {self.__nombre} | Email: {self.__email}"
