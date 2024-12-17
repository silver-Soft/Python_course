# Listas
#TODO Una lista siempre llevará llaves [...] y cada elemento es separado por comas [E1, E2, E3]
frutas = ["manzana", "banana", "cereza","naranja","pera","fresa"] 
#TODO AGREGAR UN ELEMENTO A LA LISTA
#frutas.append("naranja") 
#TODO ELIMINAR EL PRIMER ELEMENTO DE LA LISTA
#frutas.pop(0)
#TODO ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA
#frutas.pop()
#TODO ELIMINAR UN ELEMENTO POR INDICE O POCICION EN LA LISTA
#frutas.pop(2) 
#TODO ELIMINAR UN ELEMENTO POR CLAVE O VALOR
#frutas.remove("banana") 
#print("Lista de frutas:", frutas)

# Bucle principal
while True:
    # Mostrar el menú
    print("Seleccione una operación:")
    print("1. Agregar un elemento (fruta)")
    print("2. Eliminar el primer elemento")
    print("3. Eliminar el ultimo elemento")
    print("4. Eliminar elemento de una posicion de la lista")
    print("5. Eliminar elemento por clave")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == "1":
        print("Seleccionaste - Agregar un elemento.")

        entrada = input("Ingresa el nombre de la fruta que quieres agregar: ")
        frutas.append(entrada) 
        print("Nueva lista de frutas: ", frutas)

    elif opcion == "2":
        print("Seleccionaste - Eliminar el primer elemento.")
        frutas.pop(0)
        print("Nueva lista de frutas: ", frutas)

    elif opcion == "3":
        print("Seleccionaste - Eliminar el ultimo elemento.")
        frutas.pop()
        print("Nueva lista de frutas: ", frutas)

    elif opcion == "4":
        print("Seleccionaste - Eliminar elemento de una posicion de la lista.")
        posicion = int(input("Ingresa la posicion de la fruta que quieres eliminar: "))
        frutas.pop(posicion) 
        print("Nueva lista de frutas: ", frutas)

    elif opcion == "5":
        print("Seleccionaste - Eliminar elemento por clave.")
        print("Lista de frutas: ", frutas)
        entrada = input("Ingresa el nombre de la fruta que quieres eliminar: ")

        try:
            frutas.remove(entrada) 
            print("Nueva lista de frutas: ", frutas)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un valor correcto.")
                    
    else:
        print("Opción no válida.")

    # Preguntar si desea continuar
    repetir = input("\n¿Quieres realizar otra operación? (s/n): ").lower()
    if repetir != "s":
        print("¡Gracias por usar el programa!")
        break