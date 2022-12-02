#Seno, Cosseno e Tangente

'''Faça um programa que leia um 
ângulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente 
desse ângulo.'''

from math import cos, sin, tan, radians

ângulo = float(input('Digite o ângulo: '))
print (f'O ângulo de {ângulo} tem:\n'
       f'Seno de {sin(radians(ângulo)):.2f}\n'
       f'Coseno de {cos(radians(ângulo)):.2f}\n'
       f'Tangente de {tan(radians(ângulo)):.2f}')
