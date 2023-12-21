#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
contIdade = 0
contHomem = 0
contMulher = 0
while True:
    print('-'*50)
    idade= int(input( ' Idade: ').strip().replace(' ',''))
    sexo= ' '
    while sexo not in 'MF':
        sexo = input(' Sexo: ').strip().upper()[0]
    if idade > 18:
        contIdade +=1
    if sexo == 'M':
        contHomem +=1
    if idade < 20 and sexo == 'F':
        contMulher +=1
    saida= ' '
    while saida not in 'SN':
        saida = input(' Quer continuar? [S / N] ').strip().upper()
    if saida == 'N':
        break
print(f' Total de pessoas com mais de 18 anos: {contIdade}')
print(f' Ao todo temos {contHomem} homens cadastrados. ')
print(f' E temos {contMulher} mulheres com menos de 20 anos.')