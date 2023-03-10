#La pizzería Dariannis Pizzas ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
#ingredientes para cada tipo de pizza aparecen a continuación. A) Ingredientes vegetarianos:
#Pimiento y tofu. b) Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón. Escribir un
#programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su
#respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede
#elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al
#final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
#ingredientes que lleva.

print("Receta de pizza")

def tipos():
    print("¿Qué tipo de pizza quiere? \n")
    print("1. Vegetariana")
    print("2. No vegetariana\n")

def vegetariana():
    print("\n¿De qué la desea?")
    print("1. Pimiento")
    print("2. Tofu\n")

def noVegetariana():
    print("\n¿De qué la desea?")
    print("1. Pepperoni")
    print("2. Jamón")
    print("3. Salmón\n")

tipos()

opcionTipo = input("Ingrese el número de la opción que desea \n")

while opcionTipo != "1" and opcionTipo != "2":
    print("\nIngrese una opción correcta \n")
    tipos()
    opcionTipo = input("Ingrese el número de la opción que desea \n")

if(opcionTipo == "1"):
    vegetariana()
    opcionIngrediente = input("Ingrese el número de la opción que desea \n")

    while opcionIngrediente != "1" and opcionIngrediente != "2":
        print("\nIngrese una opción correcta \n")
        vegetariana()
        opcionIngrediente = input("Ingrese el número de la opción que desea \n")

    if(opcionIngrediente == "1"):
        ingrediente = "pimiento"
    else:
        ingrediente = "tofu"

    print("\nLa pizza es vegetariana")
    print("Sus ingredientes son harina de trigo, sal, agua y levadura, cubierto con salsa de tomate, queso mozzarella y "
          + ingrediente)
else:
    noVegetariana()
    opcionIngrediente = input("Ingrese el número de la opción que desea \n")

    while opcionIngrediente != "1" and opcionIngrediente != "2" and opcionIngrediente != "3":
        print("\nIngrese una opción correcta \n")
        noVegetariana()
        opcionIngrediente = input("Ingrese el número de la opción que desea \n")

    if(opcionIngrediente == "1"):
        ingrediente = "pepperoni"
    elif(opcionIngrediente == "2"):
        ingrediente = "jamón"
    else:
        ingrediente = "salmón"

    print("\nLa pizza no es vegetariana")
    print("Sus ingredientes son harina de trigo, sal, agua y levadura, cubierto con salsa de tomate, queso mozzarella y "
          + ingrediente)