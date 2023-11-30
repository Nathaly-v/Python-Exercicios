# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for n1 in range (1, 7):
    numero= int (input ( f'Digite o valor {n1}: '))
    if numero % 2 == 0 :
        soma = soma + numero
        cont += 1
print (f' A soma dos {cont} números pares é igual: {soma}')
    