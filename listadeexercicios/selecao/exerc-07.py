'''Escreva um programa para ler 2 valores 
(considere que não serão informados valores iguais) e escrever o maior deles.'''

#entrada
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

#processamento
'''resposta = 0
if valor1 > valor2:
    resposta = valor1

else:  
    resposta = valor2'''
resposta = valor1 if valor1 > valor2 else valor2

#saída
print("O maior valor é ", resposta)
