'''Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e
escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se o
aluno foi aprovado (considere 6.0 a média mínima para aprovação).'''

#entrada
nt1 = float(input("Digite a primeira nota:"))
nt2 = float(input("Digite a segunda nota:"))

#processamento
ms = (nt1 + nt2)/2 #ms = média semestral
resposta = ""
if (ms >= 6.0):
    resposta = "Parabéns você foi APROVADO!"
else:
    resposta = "Você não foi aprovado."

#saída
print("A média semestral foi de", ms)
print(resposta)


