#En la empresa Mike & Asociados SRL, sus empleados son evaluados al final de cada año
#(Evaluación de desempeño). Los puntos que pueden obtener en la evaluación comienzan en
#0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
#conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre
#las cifras mencionadas. A continuación, se muestra una tabla con los niveles
#correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de
#2.400$ USD multiplicada por la puntuación del nivel. Escribir un programa que lea la
#puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero
#que recibirá el usuario.

print("Obtención de beneficio por evaluación de desempeño anual \n")

malo = 0.0
bueno = 0.4
excelente = 0.6

def mostrarOpciones():
    print("Menu de opciones \n")
    print("1. 0.0 ")
    print("2. 0.4")
    print("3. 0.6 \n")

mostrarOpciones()

puntuacion = input("Ingrese el numero de la opción que tiene su puntuación de desempeño anual \n")

while puntuacion != "1" and puntuacion != "2" and puntuacion != "3":
    print("\nIngrese una opción correcta \n")
    mostrarOpciones()
    puntuacion = input("Ingrese el numero de la opción que tiene su puntuación de desempeño anual \n")


if puntuacion == "1":
    print("\nSu nivel de desempeño es malo")
    print("La cantidad de dinero que recibe es: " + str(malo) + " USD$")
elif puntuacion == "2":
    print("\nSu nivel de desempeño es bueno")
    print("La cantidad de dinero que recibe es: " + str(2400 * bueno) + " USD$")
else:
    print("\nSu nivel de desempeño es excelente")
    print("La cantidad de dinero que recibe es: " + str(2400 * excelente) + " USD$")