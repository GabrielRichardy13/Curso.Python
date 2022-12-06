#Custo da Viagem

'''Desenvolva um programa que pergunte 
a distância de uma viagem em Km. Calcule 
o preço da passagem, cobrando R$0,50 por 
Km para viagens de até 200Km e R$0,45 parta 
viagens mais longas.'''

n = float(input('Qual a distância da viagem?'))

if n <= 200:
    print(f'Sua viagem vai custar: R${n * 0.5:.2f}')
else:
    print(f'Sua viagem vai custar: R${n * 0.45:.2f}')