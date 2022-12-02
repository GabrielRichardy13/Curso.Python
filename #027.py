#Jogo da Adivinhação v.1.0

'''Escreva um programa que faça 
o computador "pensar" em um número 
inteiro entre 0 e 5 e peça para o 
usuário tentar descobrir qual foi o número 
escolhido pelo computador. O programa deverá 
escrever na tela se o usuário venceu ou perdeu.'''

nome = input('Digite seu nome completo: ')
separador = nome.split()
print (f'''Muito prazer em te conhecer!!!
Seu primeiro nome é: {separador[0]}
Seu segundo nome é: {separador[-1]}''')