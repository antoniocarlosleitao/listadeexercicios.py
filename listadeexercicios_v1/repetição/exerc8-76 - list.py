'''76) Construa um algoritmo que leia 50 valores inteiros e positivos e: 
·  Encontre o maior valor 
·  Encontre o menor valor 
·  Calcule a média dos números lidos'''
#OBS 1: Refaça o exercício usando lista para armazenamento dos valores digitados pelo usuário.
#OBS 2: Faça com que o sistema sorteie 6 valores digitados pelo usuário logo após exibir a mensagem. 
#(random.range(1,51))


maior = 0 
menor = 999999999999
soma =  0
limite = 5

listValores = [] #[] representa uma lista/array

for x in range(1, limite+1): #for = repetições
    valor = int(input(f"Qual o {x}º valor?")) #x recebe os numeros e é o contador
    if(valor > maior):   #maior = ao maior valor digitado
        maior = valor   #valor = ao valor digitado
    if(valor < menor):   
        menor = valor
    soma = soma + valor #a soma esta fora do if, mas dentro do for
    print("Soma = ", soma)
    listValores.append(valor) #append acrescenta elementos a lista

print("Média = ", int(soma/limite)) #se tirar o int a conta da média será float
print("Maior número é: ", maior)
print("Maior número é: ", menor)
print("Valores: ", listValores)

for itemValor in listValores:
    if(itemValor % 2 == 0):
        print("número par: ", itemValor)

for itemValor in listValores:
    if(itemValor % 2 != 0):
        print("número impar =  ", itemValor)

listPar = []
listImpar = []

for itemValor in listValores:
    if(itemValor % 2 != 0):
        print("número impar =  ", itemValor)

