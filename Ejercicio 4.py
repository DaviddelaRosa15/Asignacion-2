#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
#cantidad a dos decimales.

print("Cálculo de cantidad de ahorros tras años")

monto = input("Ingrese la cantidad de dinero depositado en la cuenta de ahorros \n")

while monto == "" :
    print("Ingrese un valor")
    monto = input("Ingrese la cantidad de dinero depositado en la cuenta de ahorros \n")

for i in range(1,4):
    resultado = round(float(monto) * ((4/100+1)**i), 2)
    print("El resultado de la cantidad de ahorros tras el año " + str(i) + " es de: " +
           str(resultado) + " RD$")