# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome= input('Digite seu nome completo : ')

maior=nome.upper()
menor=nome.lower()

quant= len(nome.replace(' ' , ''))
quantnome= len(nome.split()[0])
pnome= (nome.split()[0])

print ('='*50)

print(f'Analisando o seu nome ... ')
print(f'Seu nome em maiúsculas {maior}. ')
print(f'Seu nome em minúsculo {menor}. ')
print(f'Seu nome tem ao todo {quant} letras. ')
print(f'seu primeiro nome é {pnome} e tem {quantnome} letras. ')

print ('='*50)
