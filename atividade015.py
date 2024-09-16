# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
op=input("qual operaçao voce deseja fazer: subtração, adição,divisão ou multiplicação?")
n1=float(input("digite o valor 1:"))
n2=float(input("digite o valor 2:"))

if (op=="subtração"):
    print(n1-n2)
elif(op=="adição"):
    print(n1+n2)
elif(op=="divisão"):
    print(n1//n2)
elif(op=="multiplicação"):
    print(n1*n2)