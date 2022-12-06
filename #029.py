#Radar eletrônico

'''Escreva um programa que leia a velocidade 
de um carro. Se ele ultrapassar 80Km/h, mostre 
uma mensagem dizendo que ele foi multado. A multa 
vai custar R$7,00 por cada Km acima do limite.'''

carro = float(input('Digite a velocidade do veículo:'))

if carro <= 79:
    print ('\33[92m Tenha um bom dia! Dirija com segurança! \33[m')
else:
    print(f'''\33[91m MULTADO! Você excedeu o limite de velocidade que é de 80km/h.
    Você deve pagar uma multa de \33[41mR${(carro - 80) * 7 :.2f} \33[0m''')