#Faça um programa que pegue informações do usuário, e identifique se ele(a) é legível com 
# base na análise, apresente a informação no terminal sobre o status dessa análise:
#Informações para Coleta
# @ Nome completo;
# @ Idade;
# @ CPF;
# @ Telefone;

# Informações para Analisar
# @ Nome completo (Não pode haver números);
# @ Idade (Precisa ser maior que 18 anos e menor que 23 anos);
# @ CPF (EX: 237.832.53(8)-02) - O terceiro último número precisa ser 8;
# @ Telefone (O DDD do número precisa ser 11);

# Contexto: Uma empresa de tecnologia está procurando jovens do estado de São Paulo para 
# oferecerem vagas de Jovem aprendiz, para isso precisamos analisar os dados inseridos 
# por eles e identificar se são legíveis ao processo de Jovem aprendiz. 

from Funcao import *
print ('+=' * 30)
print(' \n\t___ PROCESSO SELETIVO PARA JOVEM APRENDIZ ___\n')
print ('+='* 30)


nome = input ('\nDigite o seu nome completo : ').strip().upper()
resultadoNome = analisaNome(nome)
if resultadoNome == True:
    pass
    print(resultadoNome)
else:
    while resultadoNome == False:
        nome = input(' \nErro! Digite novamente: ').strip().upper()  
        resultadoNome = analisaNome(nome)      
        
idade = int(input(' \nDigite sua idade: ').strip())
resultadoIdade= analisaIdade(idade)
print(resultadoIdade)

cpf=input(' \nDigite o seu CPF:').strip()
cpfLimpo = cpf.replace('.', '').replace('-', '')
resultadoCPF= analisaCPF(cpfLimpo)
print(resultadoCPF)

telefone = input('\n Digite seu número de telefone: ').strip()
telefoneLimpo = telefone.replace('-', '')
resultadoTelefoneDDD = analisaTelefone(telefone)
print(resultadoTelefoneDDD)

if resultadoNome and resultadoIdade and resultadoCPF and resultadoTelefoneDDD:
    print(' Parábens! Você foi APROVADO no nosso processo de jovem aprendiz.')
else:
    print(' Infelizmente você NÃO está apto ao nosso processo seletivo de jovem aprendiz. ')    