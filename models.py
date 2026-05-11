
from abc import ABC, abstractmethod
import logging

# Clase Abstracta General (Requisito: Clase abstracta que represente entidades generales)
class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad

    @abstractmethod
    def obtener_detalles(self):
        pass

# Clase Cliente (Requisito: Validaciones robustas y encapsulación)
class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, email):
        super().__init__(id_cliente)
        self.__nombre = None
        self.__email = None
        self.set_nombre(nombre)
        self.set_email(email)

    def set_nombre(self, nombre):
        if not nombre or len(nombre) < 3:
            raise ValueError("Nombre de cliente inválido (mínimo 3 caracteres).")
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_email(self, email):
        if "@" not in email:
            raise ValueError("Formato de email incorrecto.")
        self.__email = email

    def obtener_detalles(self):
        return f"ID: {self.id_entidad} | Cliente: {self.__nombre} | Email: {self.__email}"
