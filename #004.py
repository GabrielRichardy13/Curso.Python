#Dissecando uma Variável

'''Faça um programa que 
leia algo pelo teclado e 
mostre na tela o seu tipo 
primitivo e todas as informações 
possíveis sobre ele.'''

algo = input('Digite algo: ')
print (f'O tipo primitivo de valor da classe é: {type(algo)}')
print (f'É Número: {algo.isnumeric()}')
print (f'É Alfabético: {algo.isalpha()}')
print (f'É alphanumérico: {algo.isalnum()}')
print (f'Está em maiúculo: {algo.isupper()}')
print (f'Está em minúscula: {algo.islower()}')
print(f'Está capitalizado: {algo.istitle()}')
