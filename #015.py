#Aluguel de Carros

'''Escreva um programa que pergunte
 a quantidade de Km percorridos por 
 um carro alugado e a quantidade de dias
  pelos quais ele foi alugado. Calcule 
  o preço a pagar, sabendo que o carro 
  custa R$60 por dia e R$0,15 por Km rodado.'''

dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

print(f'TOTAL A PAGAR: R${(dias * 60) + (km * 0.15):.2f}\n')