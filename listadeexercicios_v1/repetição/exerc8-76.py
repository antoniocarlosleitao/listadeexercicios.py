'''76) Construa um algoritmo que leia 50 valores inteiros e positivos e: 
·  Encontre o maior valor 
·  Encontre o menor valor 
·  Calcule a média dos números lidos'''
#OBS 1: Refaça o exercício usando lista para armazenamento dos valores digitados pelo usuário.
#OBS 2: Faça com que o sistema sorteie 6 valores digitados pelo usuário logo após exibir a mensagem. 
#(random.range(1,51))

maior = 0 
menor = 0
soma =  0

for x in range(1, 6):
    valor = int(input(f"Qual o {x}º valor?"))

