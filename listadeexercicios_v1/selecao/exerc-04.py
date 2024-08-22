'''Acrescente ao exercício anterior a mensagem Você foi REPROVADO! Estude mais... caso a
média calculada seja menor que 6.0.'''
#entrada
nt1 = float(input("Digite a primeira nota:"))
nt2 = float(input("Digite a segunda nota:"))

#processamento
ms = (nt1 + nt2)/2 #ms = média semestral
resposta = ""
if (ms >= 6.0):
    resposta = "Parabéns você foi APROVADO!"
else:
    resposta = "Você foi REPROVADO! Estude mais."

#saída
print("A média semestral foi de", ms)
print(resposta)



