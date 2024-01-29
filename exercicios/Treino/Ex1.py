# Faça um programa que filtre informações do usuário e insira em uma variável, o filtro precisa limpar qualquer número ou caractere especial. Ao final mostre um print do resultado sem filtro e com filtro.
# EX:
# input do usuário: Rato@ De5 Circo4
# resultado: Rato De Circo 


filtro = ''
nome = input(' Insira um nome: ')

print(f'{nome}')

for caractere in nome:  
    if caractere.isalpha():
        filtro += caractere
    elif caractere == ' ':
        filtro += caractere
print(f'{filtro}')



