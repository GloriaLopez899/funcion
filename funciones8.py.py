def largo(cadena):
    return len(cadena)

nombre1=input("Ingrese primer nombre: ")
nombre2=input("Ingrese segundo nombre: ")
la1=largo(nombre1)
la2=largo(nombre2)

if la1==la2:
    print("Los nombres: ", nombre1, nombre2, "tienen las mismas cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1, " es el más largo")
    else:
        print(nombre2, " es el más largo")

