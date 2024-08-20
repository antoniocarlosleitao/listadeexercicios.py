'''Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for
digitado o valor zero, escrever a palavra zero.'''
#entrada
valor = int(input("Escreva um valor: "))

#processamento
resposta = ""
if valor == 0:
    resposta = "zero"
elif valor > 0:            #elif = se não
     resposta = "positivo"
else:
    resposta = "negativo"

#saída
print("O valor é", resposta)
      

