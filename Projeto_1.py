# PROJETO 1 
# Módulo 1 - Gerar registro do funcionário

from datetime import datetime 
from colorama import Fore, Style
from tqdm import tqdm
from time import sleep
import random

c = (
    '\033[m',            #0 sem cor
    '\033[1;31m',        #1 vermelho
    '\033[1;42m',        #2 verde
    '\033[1;43m',        #3 amarelo
    '\033[1;44m',        #4 azul
    '\033[1;35m',        #5 roxo
    '\033[7;40m'         #6 branco
)

def linha(text):
    tam = len(text) + 4 

    print('-' * tam)
    print(text.center(tam))
    print('-' * tam)


def leia_nome(nome='<desconhecido>'):
    while True:
        try:
            n = input('Digite seu nome: ')
            
            if len(n) == 0:  # Verifica se a entrada está vazia
                print()
                raise ValueError(c[1] + 'Por favor, seu nome não pode estar vazio.' + c[0])
        except ValueError as e:
            print(f'\033[1;31mERRO: {e}\033[m')
        else:
            return n
        
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print()
            print(c[1]+'ERRO: Digite um número inteiro válido!'+c[0])
            continue
        except KeyboardInterrupt:
            print()
            print(c[1]+'O usuário preferiu não informar um número'+c[0])
            print()
            return 0
        else:
            return n


linha(c[5]+ 'OLÁ BEM VINDO A NOSSA EMPRESA' + c[0])

while True:
    # 1. Obtenha o nome e idade  do usuário
    nome = leia_nome()
    idade = leiaint('Digite sua idade:')


    #3. Registre de forma automática a data do cadastro do usuário, 
    # usando a data do registro como data de registro
    data_de_cadastro = datetime.now().strftime('%d/%m/%Y')

    #4. Para cada novo funcionário que é registrado na empresa,
    #  ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:

    cartoes = ['R$50,00','R$250,00','R$120,00']
    sorteio_de_cartoes = random.choice(cartoes)


    # 5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
    while True:
        try:
            aniversário = datetime.strptime(input('Quando será seu aniversário (dd/mm/aaa): '), '%d/%m/%Y')
            print()
        except ValueError:
            print()
            print(c[1]+ 'Formato de data inválida, por favor, siga o exemplo: (dd/mm/aaaa)' + c[0])
        
        else:
            print()
            linha(c[5]+'SALVANDO DADOS...'+c[0])
            for i in tqdm(range(5)):
                print(f'{i}', end='')
                sleep(0.5)
            print()
            break
            exit()

    ## Módulo 2 - Gerar apresentação do usuário

    ### Funcionalidades do módulo 2 - Mensagem de boas vindas!
    '''
    Usando os dados obtidos no módulo 1, exiba as seguintes informações:

    1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).

    Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
    '''
    print()
    print(f"""Olá {nome}, seu registro foi concluído com sucesso no dia {data_de_cadastro}.
Parabéns, houve um sorteio e você ganhou um cartão de comprar no valor de {sorteio_de_cartoes}""")
    print()
    sleep(1)

    linha(c[5] +'CADASTRAR UM NOVO FUNCIONÁRIO?'+c[0])
    opc = str(input('[S/N]')).strip().upper()[0]

    while opc not in 'SN':
        print(c[1] + 'opção inválida, digite uma opção válida' + c[0]) 
        opc = str(input('[S/N]')).strip().upper()[0]

    if opc == 'S':
        print()
        sleep(1)
        linha(c[5] +'NOVO CADASTRO:'+ c[0])

    if opc == 'N':
        print()
        sleep(1)
        linha(c[1] +'FINALIZANDO SISTEMA'+ c[0])
        sleep(1)
        break
    