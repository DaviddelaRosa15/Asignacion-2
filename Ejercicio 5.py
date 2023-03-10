#Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste
#final total.

print("Cálculo del total de pan menos su descuento por no ser del día \n")

habitual = 3.49
descuento = 3.49 * 0.6

cantidad = input("Ingrese la cantidad de barras de pan vendidas que no son del día \n")

while cantidad == "" :
    print("Ingrese un valor")
    cantidad = input("Ingrese la cantidad de barras de pan vendidas que no son del día \n")

total = round(int(cantidad) * (habitual - descuento), 2)

print("\nEl precio habitual de la barra de pan es: " + str(habitual) + "$")
print("El descuento que se hace por no ser del día es: " + str(round(habitual - descuento)) + "$")
print("El coste habitual es: " + str(round(int(cantidad) * habitual, 2)) + "$")
print("El coste total es: " + str(total) + "$")