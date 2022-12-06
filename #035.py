#Analisando Triângulo v1.0

'''Desenvolva um programa que leia 
o comprimento de três retas e diga 
ao usuário se elas podem ou não formar 
um triângulo.'''

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print ('Os segmentos acima \33[32mPODEM FORMAR\33[0m um triângulo. ')
else: 
    print('Os segmentos acima \33[91m NÃO PODEM FORMAR \33[0m um triângulo. ')