#Ano Bissexto

'''Faça um programa que leia 
um ano qualquer e mostre se 
ele é bissexto.'''

ano = int(input('Digite o ano ou digite 0 (zero) para saber sobre o ano atual: '))
if ano == 0:
    from datetime import date
    ano = date.today().year

if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano {ano} \33[32m É \33[0m bissexto. ')
else:
    print(f'O ano {ano} \33[91m NÃO \33[0m é bissexto.')