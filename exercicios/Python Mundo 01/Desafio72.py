# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numerosPorExtenso = ('Zero', 'Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

for cont in range(0, (numerosPorExtenso)):
    opNumeros= int(input(' Digite um número entre 0 e 20: '))
    if opNumeros >= 0 and opNumeros <= 20:
        print(f'{numerosPorExtenso[opNumeros]}')
    else:
        print('Tente novamente.', end = '')
     
        