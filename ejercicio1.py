#colaborador = int(input("Ingrese el número de colaboradores que desea que se muestre: "))

#with open("colaboradores.txt", "r") as file:
#    content = file.readlines()
#    for i in range(colaborador):
#        if i < len(content):
#            print(content[i].strip())
#        else:
#            print("No hay más colaboradores para mostrar.")
#            break
#    else:
#        print("Todos los colaboradores han sido mostrados.")




opcion = int(input("Seleccione una opción:\n1. Ingrese el número de colaboradores que desea que se muestre\n2. Mostrar todos los colaboradores\n3. Agregar nuevos colaboradores\n"))

if opcion == 1:
    colaborador = int(input("Ingrese el número de colaboradores que desea que se muestre: "))
    with open("colaboradores.txt", "r") as file:
        content = file.readlines()
        for i in range(colaborador):
            if i < len(content):
                print(content[i].strip())
            else:
                print("No hay más colaboradores para mostrar.")
                break
        else:
            print("Todos los colaboradores han sido mostrados.")
elif opcion == 2:
    with open("colaboradores.txt", "r") as file:
        content = file.readlines()
        for line in content:
            print(line.strip())
elif opcion == 3:
    with open("colaboradores.txt", "r") as file:
        content = file.readlines()
        if len(content) >= 15:
            print("Ya hay 15 colaboradores, no se pueden agregar más.")
        else:
            nuevos_colaboradores = input("Ingrese nuevos colaboradores: ")
            with open("colaboradores.txt", "a") as file:
                file.write("\n" + nuevos_colaboradores)
            print("Se ha agregado un nuevo colaborador.")
else:
    print("Opción inválida")
