# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

cont = 0
resultado = 0

while True:
    numero=int(input(' Digite um valor (999 para parar: )'))
    if numero == 999:
        break
    else:
        resultado = resultado + numero
        cont +=1
print (f' A soma dos {cont} valores foi {resultado}')