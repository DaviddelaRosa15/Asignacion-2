#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.

print("Cálculo de capital obtenido a través de la inversión que hayamos hecho \n")

monto = float(input("Ingrese la cantidad que desea invertir \n"))
interes = float(input("Ingrese el interes anual \n"))
tiempo = int(input("A cuántos años quiere la inversión \n"))

while monto == "" or interes == "" or tiempo == "":
    print("Ingrese un valor")
    monto = float(input("Ingrese la cantidad que desea invertir \n"))
    interes = float(input("Ingrese el interes anual \n"))
    tiempo = int(input("¿A cuántos años quiere la inversión? \n"))

capital = round(monto * ((interes/100+1)**tiempo), 2)
print("El capital obtenido es: " + str(capital) + " RD$")