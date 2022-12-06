#Aumentos múltiplos

'''Escreva um programa que pergunte 
o salário de um funcionário e calcule 
o valor do seu aumento. Para salários 
superiores a R$1250,00, calcule um aumento 
de 10%. Para os inferiores ou iguais, o 
aumento é de 15%.'''

salário = float(input('Qual o salário do funcionário? '))
if salário >= 1250:
    salário += salário * 10 / 100
else:
    salário += salário * 15 / 100
print (f'O salário do funcionário será de R${salário:.2f}')
