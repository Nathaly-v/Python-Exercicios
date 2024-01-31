# Faça um programa que consiga adicionar informações em um bloco de texto sem abrir o bloco de texto. Apresente essas informações no terminal.

with open('Treino/info.txt' , 'a') as arquivo:
    novaFrase= 'Conseguiiiiiii de novooooooyuuuuu!!!'
    arquivo.write(novaFrase)