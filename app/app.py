import json

# Funciones auxiliares

def cargar_datos():
    try:
        with open("finanzas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"ingresos": [], "gastos": []}

def guardar_datos(datos):
    with open("finanzas.json", "w") as archivo:
        json.dump(datos, archivo)

def obtener_total(items):
    total = 0
    for item in items:
        total += item["monto"]
    return total

def obtener_total_por_categoria(items):
    total_por_categoria = {}
    for item in items:
        categoria = item["categoria"]
        monto = item["monto"]
        if categoria in total_por_categoria:
            total_por_categoria[categoria] += monto
        else:
            total_por_categoria[categoria] = monto
    return total_por_categoria

# Funciones principales

def menu():
    print("---- MENÚ ----")
    print("1. Capturar ingreso")
    print("2. Capturar gasto")
    print("3. Reporte de gastos por categoría")
    print("4. Reporte de ingresos por categoría")
    print("5. Reporte general")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

def capturar_ingreso():
    ingreso = {}
    ingreso["concepto"] = input("Concepto del ingreso: ")
    ingreso["monto"] = float(input("Monto del ingreso: "))
    ingreso["categoria"] = input("Categoría del ingreso: ")
    datos = cargar_datos()
    datos["ingresos"].append(ingreso)
    guardar_datos(datos)
    print("Ingreso registrado exitosamente.")

def capturar_gasto():
    gasto = {}
    gasto["concepto"] = input("Concepto del gasto: ")
    gasto["monto"] = float(input("Monto del gasto: "))
    gasto["categoria"] = input("Categoría del gasto: ")
    datos = cargar_datos()
    datos["gastos"].append(gasto)
    guardar_datos(datos)
    print("Gasto registrado exitosamente.")

def reporte_gastos_por_categoria():
    datos = cargar_datos()
    gastos = datos["gastos"]
    total_por_categoria = obtener_total_por_categoria(gastos)
    print("Reporte de gastos por categoría:")
    for categoria, total in total_por_categoria.items():
        print(f"{categoria}: ${total}")

def reporte_ingresos_por_categoria():
    datos = cargar_datos()
    ingresos = datos["ingresos"]
    total_por_categoria = obtener_total_por_categoria(ingresos)
    print("Reporte de ingresos por categoría:")
    for categoria, total in total_por_categoria.items():
        print(f"{categoria}: ${total}")

def reporte_general():
    datos = cargar_datos()
    ingresos = datos["ingresos"]
    gastos = datos["gastos"]
    total_ingresos = obtener_total(ingresos)
    total_gastos = obtener_total(gastos)
    balance = total_ingresos - total_gastos
    print("Reporte general:")
    print(f"Total de ingresos: ${total_ingresos}")
    print(f"Total de gastos: ${total_gastos}")
    print(f"Balance: ${balance}")
    

def main():
    # Cargar los datos desde los archivos JSON
    cargar_datos()

    # Ciclo principal del programa
    while True:
        opcion = menu()

        if opcion == "1":
            capturar_ingreso()
        elif opcion == "2":
            capturar_gasto()
        elif opcion == "3":
            reporte_gastos_por_categoria()
        elif opcion == "4":
            reporte_ingresos_por_categoria()
        elif opcion == "5":
            reporte_general()
        elif opcion == "6":
            # Guardar los datos en los archivos JSON
            guardar_datos()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()


