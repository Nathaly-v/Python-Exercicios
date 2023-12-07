# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

c=0
idades= 0
quantPessoa=0
idadehomemVelho=0
nomeHomemVelho=0
idadeMulher=0
idademnova=0
for _ in range (1, 5):
    c+=1
    print ('-'*5 + f' {c}ª PESSOA '+ '-'*5 )
    nome =(input(' NOME : '))
    idade =int(input(' IDADE : ')) 
    idades = idades + idade
    sexo=(input(' SEXO [ M/F] ')).upper()
    if _==1 and sexo == 'M':   
        nomeHomemVelho=nome
        idadeHomemVelho=idade
    elif idade > idadeHomemVelho and sexo == 'M':
        idadeHomemVelho=idade
        nomeHomemVelho=nome

    elif idade < 20:
        idademnova+=1
        
    quantPessoa= quantPessoa + 1
media= idades/quantPessoa    

print(f' A média de idade do grupo é de {media} anos. ')
print(f' O homem mais velho tem {idadeHomemVelho} e se chama {nomeHomemVelho}. ')
print(f' Ao todo são {idademnova} mulheres com menos de 20 anos. ')