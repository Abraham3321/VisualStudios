print("Calculadora  Simple")
numero1 = float(input("Dame el primer numero: "))
numero2 = float(input("Dame el segundo numero: "))

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"
operacion = ""
while operacion != "5":
    operacion = input("¿Qué operación deseas realizar? (1: suma, 2: resta, 3: multiplicacion, 4: division, 5: salir): ")
    if operacion == "1":
        print(suma(numero1, numero2))
    elif operacion == "2":
        print(resta(numero1, numero2))
    elif operacion == "3":
        print(multiplicacion(numero1, numero2))
    elif operacion == "4":
        print(division(numero1, numero2))
    elif operacion == "5":
        print("¡Gracias por usar la calculadora!")
    else:
        print("Operación no válida")



