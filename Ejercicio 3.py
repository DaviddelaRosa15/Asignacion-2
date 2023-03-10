#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
#paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
#cada paquete a demanda. Cada payaso pesa 112 LB y cada muñeca 75 LB. Escribir un
#programa que lea el número de payasos y muñecas vendidos en el último pedido y
#calcule el peso total del paquete que será enviado.

print("Cálculo de peso total del paquete")

muñeca = 75
payaso = 112

ctdMuñeca = input("Ingrese la cantidad de muñecas enviados en el último paquete \n")
ctdPayaso = input("Ingrese la cantidad de payasos enviados en el último paquete \n")

while ctdMuñeca == "" or ctdPayaso == "":
    print("Ingrese un valor")
    ctdMuñeca = input("Ingrese la cantidad de payasos enviados en el último paquete \n")
    ctdPayaso = input("Ingrese la cantidad de muñecas enviados en el último paquete \n")

peso = (int(ctdMuñeca) * muñeca) + (int(ctdPayaso) * payaso)

print("El peso total del último envio es de " + str(peso) + " lbs")