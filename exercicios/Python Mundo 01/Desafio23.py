# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n1= input('Informe um número : ')

milhar= (n1[0])
centena=  (n1[1])
dezena= (n1[2])
unidade=  (n1[3])

print (f' Analisando o número : {n1}. ')

print ('='*50)

print (f' - Milhar : {milhar}. ')
print (f' - Centena : {centena}. ')
print (f' - Dezena : {dezena}. ')
print (f' - Unidade : {unidade}. ')


print ('='*50)