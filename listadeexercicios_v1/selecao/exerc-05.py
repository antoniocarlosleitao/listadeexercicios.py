'''Escreva um programa para ler um valor e escrever se é positivo ou negativo. 
Considere o valor zero como positivo.'''

#entrada
valor = float(input("Escreva um valor: ").replace(",","."))

#processamento
resposta = ""
if valor >= 0:
    resposta= "positivo"
#saída
else:
    resposta = "negativo"

#saída
print("O valor é", resposta)
      
