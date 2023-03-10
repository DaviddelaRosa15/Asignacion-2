#Para tributar (pagar impuesto DGII) un determinado impuesto se debe ser mayor de 18 años
#y tener unos ingresos iguales o superiores a 35,000 mensuales. Escribir un programa que
#pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario
#tiene que tributar o no. 

print("Comprobación del pago de impuestos \n")

edad = input("Ingrese su edad \n")
salario = input("Ingrese su salario \n")


while edad == "" or salario == "":
    print("\nIngrese un valor")
    edad = input("Ingrese su edad \n")
    salario = input("Ingrese su salario \n")

if(int(edad) >= 18 and float(salario) >= 35000):
    print("\nUsted debe pagar impuestos")
else:
    print("\nUsted no paga impuestos")
