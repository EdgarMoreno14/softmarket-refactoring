from abc import ABC, abstractmethod
from typing import List

# 1. Single Responsibility & Open/Closed Principle
class EstrategiaImpuesto(ABC):
    @abstractmethod
    def calcular(self, monto_base: float) -> float:
        pass

class ImpuestoIVA(EstrategiaImpuesto):
    def calcular(self, monto_base: float) -> float:
        return monto_base * 0.19

class RetencionFuente(EstrategiaImpuesto):
    def calcular(self, monto_base: float) -> float:
        return monto_base * 0.035

# 2. Dependency Inversion Principle
class CalculadoraFactura:
    def __init__(self, estrategias: List[EstrategiaImpuesto]):
        self.estrategias = estrategias

    def calcular_total_impuestos(self, monto_base: float) -> float:
        total = 0.0
        for estrategia in self.estrategias:
            total += estrategia.calcular(monto_base)
        return total

# 3. Módulo de uso / Integración
class Factura:
    def __init__(self, id_factura: int, cliente: str, monto_base: float):
        self.id_factura = id_factura
        self.cliente = cliente
        self.monto_base = monto_base

    def procesar(self, calculadora: CalculadoraFactura) -> dict:
        total_impuestos = calculadora.calcular_total_impuestos(self.monto_base)
        total_pagar = self.monto_base + total_impuestos
        return {
            "id": self.id_factura,
            "cliente": self.cliente,
            "subtotal": self.monto_base,
            "impuestos": total_impuestos,
            "total": total_pagar
        }
#codigo nuevo
