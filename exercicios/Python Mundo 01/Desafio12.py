# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = (float (input('Qual é o preço do produto? ')))

desconto= produto - ( produto * 5 /100)

print (f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${desconto :.2f}')