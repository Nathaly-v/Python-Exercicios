# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*50)
print('BANCO SIMULATOR')
print('='*50)
nota50 = 0
nota20 = 0
nota10 = 0
nota1  = 0

while True:
    valor=int(input(' Que valor você deseja sacar? '))
    break
while valor >= 50:
    valor = valor - 50
    nota50 +=1 
while valor >= 20:
    valor = valor - 20
    nota20 +=1    
while valor >= 10: 
    valor = valor - 10
    nota10 +=1
while valor >= 1:
    valor = valor - 1
    nota1 += 1
  

if nota50 > 0:
    print(f' Total de {nota50} cédulas de R$ 50,00') 
if nota20 > 0:   
    print(f' Total de {nota20} cédulas de R$ 20,OO')
if nota10 > 0:  
    print(f' Total de {nota10} cédulas de R$ 10,00')
if nota1 > 0:
    print(f' Total de {nota1} cédulas de R$ 1,00') 