#Par ou Ímpar?

'''Crie um programa que leia um 
número inteiro e mostre na tela 
se ele é PAR ou ÍMPAR.'''

n = int(input('\33[35m Digite um número: \33[0m'))

if n % 2 == 0:
    print (f'O número {n} é um número \33[33m PAR.\33[0m')
else:
    print (f'O número {n} é um número \33[32m ÍMPAR. \33[0m')
