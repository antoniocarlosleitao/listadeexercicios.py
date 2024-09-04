import random
import os
from colorama import Fore # type: ignore


def volante():
    return list(range(1, 61))


def sortear():
    listaSort = random.sample(volante(), 6)
    return sorted(listaSort)


def aposta():
    jogo = []
    print("Digite apenas números inteiros entre 1 e 60!")
    while True:
        try:
            for i in range(1, 7):
                num = int(input(f"Digite o {i}º número: "))
                while True:
                    if num > 60:
                        print("A mega sena só aceita números menores ou igual a 60")
                        num = int(input(f"Digite o {i}º número: "))
                    elif num <= 0:
                        print("0 ou números negativos não são permitidos.")
                        num = int(input(f"Digite o {i}º número:"))
                    elif num in jogo:
                        print("Este número já foi digitado!")
                        num = int(input(f"Digite o {i}º número:"))
                    else:
                        jogo.append(num)
                        break
            os.system("cls")
            return sorted(jogo)
        except ValueError:
            print("Valor inválido, digite apenas números inteiros entre 1 e 60!")


def acerto(jogo, resposta):
    acert = 0
    for i in jogo:
        if i in resposta:
            acert += 1
    return acert


def ganhador(acert):
    if acert == 6:
        return "Parabéns Você é o Ganhador da Mega Sena!!!"
    elif acert == 5:
        return "Parabéns Você Acertou 5 Dezenas e Ganhou a Quina da Mega Sena!!! "
    elif acert == 5:
        return "Parabéns Você Acertou 4 Dezenas e Ganhou a Quadra da Mega Sena!!! "
    else:
        return "Ainda não foi desta vez, continue tentando!!!"
    

while True:
    os.system("cls")

    print("Vamos fazer uma aposta na MEGA SENA!\n\n")
    resp1 = str(
        input("Você quer digitar ou gerar um jogo(D ou G)").lower())
        
    if resp1 == "d":
        jogo = aposta()
    elif resp1 == "g":
        jogo = random.sample(volante(), 6)

    resposta = sortear()
    pont = acerto(jogo, resposta)
    print("\n")
    print(f"Números sorteados:{resposta}")
    print(f"Seu jogo:{jogo}")
    print("\n")
    print(f"Você teve um total de {pont} acertos")
    print(ganhador(pont))
    print("\n")

    resp2 = str(input("Você quer fazer outro jogo? (S ou N)").lower())
    if resp2 == "n":
        print("Fim do programa!")
        break
    else:
        os.system("cls")