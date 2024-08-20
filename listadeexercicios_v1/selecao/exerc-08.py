'''Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que
diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).'''

from datetime import date

#entrada
an = int(input("Qual o ano do seu nascimento? "))
AA = date.today().year

#processamento
ia = AA - an
resposta = ""
if ia > 16:
    resposta = "Pode votar"
else:
    resposta = "Não pode votar"

#saida
print (resposta) 
print("porque você tem", ia, "anos")
