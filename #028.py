#Jogo da Adivinhação v.1.0

'''Escreva um programa que faça o 
computador "pensar" em um número inteiro 
entre 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo 
computador. O programa deverá escrever 
na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
computador = randint(0, 5)
print (f'''=-=-=-=-=-=-=-==-=-==-=-=-=-=-=-=-=-=-=
Vou pensar em um número entre 0 e 5...
=-=-=-=-=-=-=-==-=-==-=-=-=-=-=-=-=-=-=''')
sleep(3)
jogador = int(input('Em qual número eu pensei? '))

if computador == jogador:
    print('Parabéns você acertou!!!')
else: 
    print('Você errou!!!')