# Lista de diccionarios
frutas = [
    {"nombre": "manzana", "color": "rojo", "precio": 1.2},
    {"nombre": "banana", "color": "amarillo", "precio": 0.5},
    {"nombre": "cereza", "color": "rojo", "precio": 2.5},
    {"nombre": "naranja", "color": "naranja", "precio": 1.0}
]

fruta = input("De que futa deseas obtener el precio: ").lower()

# Intentamos encontrar la fruta en la lista
try:
    for i in range(len(frutas)):
        if fruta == frutas[i]["nombre"].lower():  # Comparar sin importar mayúsculas/minúsculas
            #TODO la f al inicio de la cadena te permite formatear de manera mas fácil variables dentro de lasalida de consola usnado {variable}
            print(f"El precio de la {frutas[i]['nombre']} es de = ${frutas[i]['precio']:.2f}")
            break
    else:
        # Si no se encuentra la fruta
        print("Fruta no encontrada.")
except ValueError:
    print("Entrada no válida. Por favor, ingrese un valor correcto.")

# Imprimir la lista de diccionarios
#print(frutas)
#for i in range(len(frutas)):
    #print(f"Producto: {i}: {frutas[i]}")