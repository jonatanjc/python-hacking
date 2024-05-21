
def mostrar_tareas(tareas):
    print("Tareas pendientes:")
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

tareas_pendientes = []

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas pendientes")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Introduce la nueva tarea: ")
        tareas_pendientes.append(tarea)
        print("Tarea agregada")
    elif opcion == "2":
        if not tareas_pendientes:
            print("No hay tareas para eliminar.")
        else:
            mostrar_tareas(tareas_pendientes)
            indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
            if 0 <= indice < len(tareas_pendientes):
                tarea_eliminada = tareas_pendientes.pop(indice)
                print(f"Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Índice de tarea inválido.")
    elif opcion == "3":
        mostrar_tareas(tareas_pendientes)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
