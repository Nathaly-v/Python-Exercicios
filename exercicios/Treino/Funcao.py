import re
        
def analisaNome(nome):       
    return bool(re.match('^[a-zA-ZÀ-ÿ\s]+$', nome))


def analisaIdade(idade):
    if idade >= 18 and idade <= 23:
        return True
    else:
        return False
                
def analisaCPF(cpf):
    if len(cpf) == 11 :
        if cpf [8] == '8':
            return True
        else: 
            return False
    else:
        while True:
            print('ERRO! Tem mais de 11 dígitos.')
            break

def analisaTelefone(telefone):
    if telefone [0:2] == '11':
        return True
    else:
        return False
               