#Simulação de sorteio da Mega-Sena
#Desenvolva um programa em sua linguagem de programação que simule o sorteio de um concurso da Mega-Sena.

#A Mega-Sena é uma loteria onde 6 números diferentes são sorteados de um conjunto de 60 números (de 1 a 60). 
#O programa deve atender aos seguintes requisitos:

# 1 Geração de números sorteados:
#Gere aleatoriamente 6 números distintos entre 1 e 60.
#Exiba esses números na tela em ordem crescente.

# 2 Entrada do usuário:
#Pedir que você insira sua aposta, que é composta por 6 números distintos entre 1 e 60.

# 3 Verificação de respostas corretas:
#Compare os números sorteados com os números que você aposta.
#Vou te dizer quantos números você acertou.

# 4 Prêmios:
#Vou mostrar o número de acertos e, de acordo com as regras da Mega-Sena, indicar o prêmio fictício:
# 4 hits: Quadra
# 5 acertos: Quina
# 6 acertos: Sena
#Se você não tiver pelo menos 4 acertos, exibirei uma mensagem informando que você não ganhou.

# 5 Repita: (Opcional)
#Vou perguntar se você deseja realizar um novo sorteio. Em caso afirmativo, reinicie o processo; 
#Caso contrário, encerre o programa.

#Dicas
#Use funções para separar a lógica de geração de números, inserção de dados do usuário e verificação de respostas corretas.
#Use estruturas de repetição para validar a entrada do usuário e garantir que 6 números válidos e distintos sejam inseridos.
#Use Arrays/List para armazenar os dados de desenho.

import random


jogo = []

def aposta():
    jogo = []
    for i in range(1,7):
        num = int(input(f"Qual o {i}º número: "))
        jogo.append(num)
    return sorted(jogo)

def volante():
    lista = []
    for i in range(1, 61):
        lista.append(i)
    return lista 

def sortear():
    listaSort = random.sample(volante(), 6)
    return sorted(listaSort)

def acerto():
    global jogo
    jogo = aposta()
    resolta = sortear()
    acert = 0
    for i in jogo:
        for x in resolta:
            if i ==x:
                acert += 1
    return acert

pont = acerto()

print("/n")
print(sortear())
print(jogo)
print("/n")
print(f"Você teve um total de {pont} acertos")


