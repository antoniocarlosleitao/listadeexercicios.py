'''Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do
combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (Km) no início do
dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$)
recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.'''

#entrada
c =  float(input("Qual o valor do litro de combustível? "))
ki = int(input("Qual a kilometragem incial do veículo? "))
kf = int(input("Qual a kilometragem final do veículo? "))
vr = int(input("Qual o valor recebido pelo percurso? "))
la = float(input("Qual o número de litros abastecido antes de iniciar o percurso? "))

#processamento
mc = ((kf-ki)/la) #cálculo da média do consumo do veículo
co = mc * c       #custo operacional
lo = vr - co      #cálculo lucro operacional no percurso

#saída
print("A média do consumo do veículo é: ", mc)
print("O lucro operacional do veículo para o percurso é: ", lo)
