# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120


numero=int(input(' Digite um número para \n Calcular o seu fatorial: '))

cont=numero -1
resultado=0


while cont > 1:
    if cont == numero -1:
        resultado = numero * cont
    else:
        resultado = resultado * cont
    cont = cont -1
print(f' {numero}! = {numero}', end = '')    
for i in range (numero - 1, 0, -1):          
    print(f' x {i}', end = '')
print(f'= {resultado}', end = ' ')