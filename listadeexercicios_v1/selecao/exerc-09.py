'''As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem
compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e
escreva o valor total da compra.'''

#entrada
nmacas = int(input("Quantas maças há na cesta? "))
vmacas12 = 0.25
vmacas11 = 0.30

#processamento
if nmacas >= 12:
    resposta = (nmacas * vmacas12)
else:
    resposta = (nmacas * vmacas11)


#saída
print("O valor a pagar será de R$", resposta,)
