#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por
#pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
#índice de masa corporal calculado redondeado con dos decimales

print("Cálculo de indice de masa corporal \n")

peso = float(input("Ingrese su peso en klogramos: \n"))
estatura = float(input("Ingrese su estatura en metros: \n"))

while peso == "" or estatura == "":
    print("Ingrese un valor")
    peso = input("Ingrese su peso en klogramos: \n")
    estatura = input("Ingrese su estatura en metros: \n")

imc = peso/(estatura**2)
imc = round(imc, 2)
print("\nTu indice de masa corporal es", str(imc))