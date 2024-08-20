'''Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e
altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas
paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de
azulejos possui 1,5 m2'''

#entrada
c = float(input("Qual o comprimento em metros? "))
l = float(input("Qual a largura em metros? "))
a = float(input("Qual a altura em metros? "))
r = 1.5 #metro quadrado por caixa de embalagem

#processamento
area = ((c*l)*a)     
nc = area/r
#saída
print("A dimensão da cozinha retangular será: ", area)
print("O número de caixas de azulejos necessarias serão:", nc)