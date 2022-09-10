print("Ingresa el primer valor: ")
valor1 = int(input())
print("Ingresa el segundo valor: ")
valor2 = int(input())
print("Ingresa el tercer valor: ")
valor3 = int(input())

print(" ")
print("El valor mayor de los tres números es: ")

if(valor1>valor2 and valor1>valor3):
    print(valor1)
elif(valor2>valor1 and valor1>valor3):
    print(valor2)
elif(valor3>valor1 and valor1>valor2):
    print(valor3)

