#Primeira e última ocorrência de uma string

'''Faça um programa que leia uma frase 
pelo teclado e mostre quantas vezes aparece 
a letra "A", em que posição ela aparece a 
primeira vez e em que posição ela aparece 
a última vez.'''

frase = input('Digite uma frase: ').strip().upper()
aparece = frase.count('A')
posição1 = frase.find('A') + 1
posição2 = frase.rfind('A') + 1
print (f'A letra A aparece {aparece} vezes na frase')
print (f'A primeira letra A aparece na posição {posição1}')
print (f'A última letra A aparece  na posição {posição2}')
