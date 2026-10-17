# CODIGO PREVIO: Función monolítica que viola múltiples principios SOLID
class GestorFactura:
    def procesar_factura(self, monto: float, tipo_impuesto: str):
        # Violación de SRP: Lógica de negocio mezclada con condicionales
        if tipo_impuesto == "IVA_GENERAL":
            total = monto * 1.19
        elif tipo_impuesto == "RETENCION_FUENTE":  # Violación OCP
            total = monto - (monto * 0.035)
        else:
            total = monto

        # Violación DIP: Dependencia rígida de una base de datos específica
        import sqlite3
        conn = sqlite3.connect("facturas.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO facturas VALUES (?)", (total,))
        conn.commit()

        print(f"Notificación enviada: Factura por {total} procesada")
