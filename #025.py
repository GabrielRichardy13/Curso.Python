#Procurando uma string dentro de outra

'''Crie um programa que leia o 
nome de uma pessoa e diga se ela tem 
"SILVA" no nome.'''

nome = input('Qual o seu nome completo? ').strip().upper()
rp = 'SILVA' in nome
print (f'Seu nome tem Silva? {rp}')