#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
#Minúsculas.

print("Validación de contraseña de usuario \n")

contraseña = "NoImporta"

valor = input("Ingrese la contraseña guardada para entrar al sistema \n")

while valor == "" :
    print("Ingrese un valor")
    valor = input("Ingrese la contraseña guardada para entrar al sistema \n")

while(contraseña.lower() != valor.lower()):
    print("\nIngrese la contraseña correcta")
    valor = input("")


print("\nBienvenido al sistema")