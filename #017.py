#Catetos e Hipotenusa

'''Faça um programa que leia o 
comprimento do cateto oposto e do 
cateto adjacente de um triângulo 
retângulo. Calcule e mostre o 
comprimento da hipotenusa.'''

cat1 = float(input('Cateto oposto: '))
cat2 = float(input('Cateto adjacente: '))
hipo = ((cat1 ** 2) + (cat2 ** 2)) ** (1/2) 
print (f'A hipotenusa de {cat1} e {cat2} é {hipo:.2f} ')