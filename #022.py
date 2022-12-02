#Analisador de Textos

'''Crie um programa que leia o nome 
completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = input('Digite o seu nome completo: ').strip()
espaços = nome.count(' ')
print (f'Seu nome em maiúculo é: {nome.upper()}')
print (f'Seu nome em minúsculos: {nome.lower()}')
print (f'Seu nome tem ao todo {len(nome) - espaços}')
separa = nome.split()
print (f'O seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')
