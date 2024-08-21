"""A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de
seu carro para que ele possa percorrer um determinado número de voltas até o primeiro
reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de
voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de
combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para
percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os
abastecimentos é o mesmo."""

#entrada
comprimento = float(input("Comprimento da pista (em metros) "))
nvoltas = int(input("numero total de voltas "))
abastecimento = int(input("numero de abastecimentos desejados "))
consumo = float(input("consumo de combustível do carro (km/l) "))


#processamento
#kmTotal = (comprimento / 1000) * nvoltas
# consumoTotal = kmTotal / consumo 
#litros = consumoTotal / abastecimento

def calculoLitros():
    kmTotal = (comprimento / 1000) * nvoltas
    consumoTotal = kmTotal / consumo 
    return consumoTotal / abastecimento

#saída
print("o número mínimo de litros necessários até o primeiro reabastecimento", calculoLitros())


