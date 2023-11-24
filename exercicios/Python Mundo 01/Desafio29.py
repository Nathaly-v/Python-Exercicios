# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
normal = "\033[0m" # to come back to default

print('-=-'*10)
print (red+'          RADAR ! '+normal)
print('-=-'*10)


velocidade= float (input(yellow +'Qual a velocidade atual do seu carro ? '+ normal))

multa= (velocidade - 80 ) * 7
print (('.'*10) + ( 'PROCESSANDO' )+('.'*10))
sleep(2)

if velocidade > 80:
    print (red + f' MULTADO ! Você excedeu o limite permitido que é de 80Km/h. ')
    print (f' Você deve pagar uma multa de R${multa} ! ' +normal)
    print (green +f' Tenha um BOM DIA!'+ normal + purple + ' Dirija com segurança ! ' +normal)
    
else: 
    print (green +f' Está dentro do limite ! Tenha um BOM DIA!'+ normal + purple + ' Dirija com segurança ! ' +normal)
    