#Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área (Pi * (raio * raio)

#entrada
raio = float(input("Qual o raio? "))
#PI = 3.14

#processamento
#area = PI*(raio*raio)
def calculoArea(valorRaio): #valorRaio é parametro para desacoplar a função para usar a função em outro código por exemplo.
    PI = 3.14 #constante
    return PI*(valorRaio * valorRaio)


#saída
#print("Area do circulo  = " , area)
#print("Area do circulo  = " + str (area))
print("Area do circulo è:", calculoArea(raio))

