'''Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).'''

from datetime import date

#entrada
an = int(input("Qual o ano do seu nascimento? "))
#AA = date.today().year

#processamento
def verificarOpcaoVoto(idadeUser):
    #ia = AA - an
    #resposta = ""
    if (idadeUser > 16):
        #resposta = "Pode votar"
        return "Pode votar"
    else:
        #resposta = "Não pode votar"
        return "Não pode votar"
    
def idade(an):                  #função testa idade, acoplada a função da linha 11 
    AA = date.today().year
    return AA - an

idadeatualUser = idade(an)

#saida
print (verificarOpcaoVoto(idadeatualUser))
print("porque você tem", idadeatualUser, "anos")
