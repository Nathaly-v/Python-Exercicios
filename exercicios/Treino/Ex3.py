#Faça um programa que consiga ler informações em um bloco de texto. Apresente essas informações no terminal.

with open('Treino/info.txt' , 'r') as arquivo:
    conteudo = arquivo.read()
print(f'{conteudo}')