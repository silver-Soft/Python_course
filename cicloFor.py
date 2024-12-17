# Ciclo for

print("Seleccione una opcion:")
print("1. Ciclo for simple de 0 a 4")
print("2. Ciclo for de 0 a tamaño de una lista")
print("3. ciclo for de N a N")

opcion = input("Ingrese el número de la operación que desea realizar: ")

# Punto de control con condicionales
if opcion == "1":
    print("Seleccionaste Ciclo for de 0 a 4.")
    for i in range(0, 4):
        print(f"Número {i}")

elif opcion == "2":
    print("Seleccionaste Ciclo for de 0 a tamaño de una lista.")
    frutas = ["manzana", "banana", "cereza","naranja","pera","fresa"] 

    for i in range(len(frutas)):
        print(f"Elemento en el índice {i}: {frutas[i]}")

elif opcion == "3":
    print("Seleccionaste ciclo for de N a M.")
    #TODO Ambos input tienen un error de tipo de dato, las entradas son string y deben ser enteras, es necesario hacer un cast int(...)
    numero1 = input("Ingrese el número inicial: ")
    numero2 = input("Ingrese el número final: ")
    for i in range(numero1, numero2):
        print(f"Número {i}")
else:
    print("Opción no válida.")


