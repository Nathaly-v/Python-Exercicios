# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont = 0
resultado = 0
numeroMaior = 0
numeroMenor = 0
while True:
    numero= int(input(' Digite um número: '))
    resultado = resultado + numero
    cont +=1   
     
    if cont == 1:
        numeroMaior = numero
        numeroMenor = numero
    elif numero > numeroMaior:
        numeroMaior = numero
    elif numero < numeroMenor:
        numeroMenor = numero
    saida = input(' Quer continuar? [ S/N ]').strip().upper()
    if saida == 'N':
        break
resultado = resultado / cont 
   
print (f'Você digitou {cont} números e a  média foi de {resultado}.')   
print (f' O maior valor foi {numeroMaior} e o menor foi {numeroMenor}.')
    