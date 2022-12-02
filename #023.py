#Separando dígitos de um número

'''Faça um programa que leia um 
número de 0 a 9999 e mostre na tela 
cada um dos dígitos separados.'''

num = int(input('Informe um número: '))
print (f'Analizando o número {num}')
print (f'A unidade é: {num // 1 % 10}')
print (f'A dezena é: {num // 10 % 10}')
print (f'A centena é: {num // 100 % 10}')
print (f'A unidade de milhar é: {num // 1000 % 10}')