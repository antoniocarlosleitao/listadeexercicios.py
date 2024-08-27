'''Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
escrevê-los em ordem crescente.'''

#entrada
valores = []
valores.append(int(input("Digite o primeiro valor: ")))  #5
valores.append(int(input("Digite o segundo valor: ")))   #2
valores.append(int(input("Digite o terceiro valor: ")))  #7

'''#processamento
resposta = ""
valorTemp = 0

def trocaNumeros(valorOrigin, valorDestino):
    valorTemp = valorDestino
    valorDestino = valorOrigin
    valorOrigin = valorTemp
    return[valorOrigin, valorDestino]  #[] = list

if(valor1 > valor2):
    resposta = trocaNumeros(valor1, valor2)
    valor1 = resposta[0]
    valor2 = resposta[1]
    # valorTemp = valor2
    # valor2 = valor1
    # valor1 = valorTemp

if(valor1 > valor3):
    resposta = trocaNumeros(valor1, valor3)
    valor1 = resposta[0]
    valor3 = resposta[1]
    # valorTemp = valor3
    # valor3 = valor1
    # valor1 = valorTemp

if(valor2 > valor3):
    resposta = trocaNumeros(valor2, valor3)
    valor2 = resposta[0]
    valor3 = resposta[1]
     # valorTemp = valor3
    # valor3 = valor2
    # valor2 = valorTemp'''

#saída
print(valores)