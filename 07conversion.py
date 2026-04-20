numero = "10"
numero_convertido = int(numero)
print(numero_convertido)
print(type(numero_convertido))

numero = "3.14"
numero_decimal = float(numero)
print(numero_decimal)
print(type(numero_decimal))

edad = 25
edad_str = str(edad)
print(edad_str)
print(type(edad_str))

print(bool (0)) # False
print(bool (1)) # True
print(bool ("")) # False
print(bool ("Hola")) # True

edad = input("Ingresa tu edad: ")
edad = int(edad)

edad_futura = edad + 5
print("En 5 años tendrás:", edad_futura)

mensaje = "Tu edad es: " + str(edad) + " y en 5 años tendras: " + str(edad_futura)
print(mensaje)