
lista=[10, 56, 23, 120, 94]
print("La lista completa es: ", lista)

def sumarizar(lista):
    suma = 0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
print("La suma de todos sus elementos es", sumarizar(lista))

def mayor(lista):
    may=lista[0]
    for x in range(len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may
print("El mayor valor de la lista es: ", mayor(lista))

def menor(lista):
    men=lista[0]
    for x in range(len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men
print("El menor valor de la lista es: ", menor(lista))



