#Reajuste Salarial 

'''Faça um algoritmo que leia 
o salário de um funcionário e 
mostre seu novo salário, com 15% 
de aumento.'''

n = float(input('Digite o seu salário: R$'))
print (f'O seu salário com 15% de aumento é R${n + (n * 15 / 100):.2f}')