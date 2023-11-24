# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = (float(input('Quanto dinheiro você tem na carteira? ')))
x1 = dinheiro / 4.91

print ('='*50)

print (f'com {dinheiro} você pode comprar US${x1:.2f}')

print ('=' *50)