# Curso: Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# Problema 3: Reabastecimiento de inventario

# R2, R3 y R7: Función que compara stocks y calcula la cantidad exacta a pedir
def calcular_cantidad_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# R4 y R7: Función que determina explícitamente si es necesario reabastecer
def requiere_reabastecimiento(cantidad_pedir):
    if cantidad_pedir > 0:
        return "Sí (Reabastecer)"
    else:
        return "No (Stock suficiente)"

def main():
    # R1: Matriz con al menos 5 artículos [Código, Nombre, Stock actual, Stock mínimo]
    inventario = [
        ["ART-001", "Teclado Mecánico USB", 8, 15],
        ["ART-002", "Mouse Inalámbrico Óptico", 25, 20],
        ["ART-003", "Monitor LED 24 Pulgadas", 4, 10],
        ["ART-004", "Cable HDMI 2 Metros", 30, 30],
        ["ART-005", "Memoria USB 64 GB", 12, 25]
    ]

    print("====================================================================================")
    print("                    INFORME DE REABASTECIMIENTO DE INVENTARIO                       ")
    print("====================================================================================")

    # R7: Estructura repetitiva para recorrer cada artículo de la matriz
    for articulo in inventario:
        nombre_articulo = articulo[1]  # R5: Nombre del artículo
        stock_actual = articulo[2]     # Stock actual
        stock_minimo = articulo[3]     # Stock mínimo requerido

        # Llamado a las funciones modulares
        cantidad_solicitar = calcular_cantidad_pedir(stock_actual, stock_minimo)
        estado_reabastecer = requiere_reabastecimiento(cantidad_solicitar)

        # R4, R5 y R6: Salida con nombre, estado de reabastecimiento y cantidad exacta
        print(f"Artículo: {nombre_articulo:<25} | ¿Reabastecer?: {estado_reabastecer:<21} | Pedir: {cantidad_solicitar} uds.")

if __name__ == "__main__":
    main()
