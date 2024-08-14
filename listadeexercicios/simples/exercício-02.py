'''Escreva um programa para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor 
correspondente em graus Celsius. (C = (F-32) * 5 / 9), T (° C) = ( T (° F) - 32) × 5/9 '''

#entrada
TF = int(input("Qual a temperatura em Fahrenheit?  "))
f = 32
x = 5
y = 9

#processamento
Celsius = ((TF-f)*x/y)

#saida
print("A temperatura em Celsius será de  = ", Celsius)


