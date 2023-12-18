# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). 
cont = 0
resultado = 0
continua = True

while continua:
    numero= int(input(' Digite um número [999 para parar]: '))
    resultado = resultado + numero
    cont += 1
    if numero == 999:
       resultado = resultado - 999
       cont -= 1
       continua = False
        
print (f' Você digitou {cont} números e a soma entre eles foi {resultado}.')
