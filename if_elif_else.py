#elif else 

edad = int(input("Ingresa tu edad: "))

if edad < 18: #TODO este bloque es obligatorio, es la primera condicion a evaluar
    print("Eres menor de edad")
elif 18 <= edad < 30: #TODO Puedes tener multiples bloques elif
    print("Eres un joven adulto")
elif 30 <= edad < 60:
    print("Eres un adulto")
else: #TODO Este bloque es opcional, y se ejecuta si ninguna de las condicinoes anteriores es verdadera
    print("Eres un adulto mayor")