#Conversor de Moedas

'''Crie um programa que 
leia quanto dinheiro uma 
pessoa tem na carteira e 
mostre quantos dólares ela 
pode comprar.'''

carteira = float(input('Quanto você tem na carteira? R$'))
print (f'Com R${carteira} você pode comprar U${carteira / 3.27:.2f}')