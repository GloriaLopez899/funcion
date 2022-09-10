
lista=[]
print("Números que desea ingresar")
n=int(input())
i=0
while i < n:
    print("valor numero", i+1)
    val = int(input())
    lista.append(val)
    i+=1
    
def sumarizar(lista):
    suma = 0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
print("La lista es: ", lista)

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

