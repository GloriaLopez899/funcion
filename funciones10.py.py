lista = []
cantidad = int(input("Cantidad de números: "))
mayor=0
menor=0
i = 1
while(cantidad > 0):
    numero = int(input("Ingrese valor " + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad - 1
mayor=max(lista)
menor=min(lista)

print("El valor mayor de la lista es: ", mayor)
print("El valor menor de la lista es:", menor)
