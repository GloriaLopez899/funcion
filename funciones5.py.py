lado = int(input("Ingresa el valor del lado de un cuadrado: "))

perimetro = lado * 4
superficie = lado * lado

opciones=input("Quiere calcular el perimetro o la superficie ingresar texto: perimetro/superficie? ")
          
if opciones == "perimetro":
    print("El perimetro del cuadrado es: ", perimetro)
if opciones == "superficie":
    print("El superficie del cuadrado es: ", superficie)
