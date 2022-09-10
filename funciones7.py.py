valor1=int(input("Ingrese el primer valor: "))
valor2=int(input("Ingrese el segundo valor: "))
def retornar_mayor(valor1, valor2):
    if valor1>valor2:
        mayor=valor1
    else:
        mayor=valor2
    return mayor
print(retornar_mayor(valor1, valor2))
  
