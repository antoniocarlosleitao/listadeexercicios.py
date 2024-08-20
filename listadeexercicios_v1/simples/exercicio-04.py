'''Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um
determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts),
as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é
de 18 watts por metro quadrado.'''

#entrada
plu = int(input("Potência da lâmpada utilizada (em watts): ")) 
l = float(input("Largura do cômodo (em metros): "))    
c = float(input("Comprimento do cômodo (em metros): "))     
wm = 18   #potência necessária em watts por metro quadrado

#processamento
area = (l*c)
pn = area*wm
nl = pn/plu

#saida
print("O número de lâmpadas para iluminar o cômodo é ", nl)


