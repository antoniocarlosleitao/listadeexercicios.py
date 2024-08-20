'''Escreva um programa para ler uma temperatura em graus Celsius, calcular e escrever o valor 
# correspondente em graus Fahrenheit. (F = (C × 9/5) + 32); F = C x 1,8 + 32'''

#entrada
TC = int(input("Qual a temperatura em Celsius?  "))
x = 9
y = 5
z = 32

#processamento
Fahrenheit = (((TC*(x/y))+z))

#saida
print("A temperatura em Fahrenheit será de  = ", Fahrenheit)
