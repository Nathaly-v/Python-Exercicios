# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome= input('Digite seu nome completo : ')


pnome= (nome.split()[0])
unome= (nome.split()[-1])

print ('-'*50)

print (f' - Muito prazer em te conhecer ! {nome}. ')
print (f' - Seu primeiro nome é : {pnome}. ')
print (f' - Seu último nome é : {unome}. ')

print ('-'*50)