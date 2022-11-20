#Conversor de Medidas

'''Escreva um programa que 
leia um valor em metros e o 
exiba convertido em centímetros 
e milímetros.'''

medida = float(input('Digite a medida em metros: '))
print (f'{medida / 1000}Km \n{medida / 100}hm \n{medida / 10}dam \n{medida * 10}dm \n{medida * 100}cm \n{medida * 1000}mm')
