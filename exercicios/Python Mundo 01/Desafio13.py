# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = (float(input('Qual é o Salário do Funcionário ? ')))

desconto = salario * 115 /100 

print (f'Um funcionário que ganhava R${salario}, com 15% de aumento , passa a receber {desconto :.2f}')