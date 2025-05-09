import re
from math import ceil
from os import system
from datetime import date, datetime

s_cor = '\033[m'
ng = '\033[1m'
vermelho = '\033[1;31m'
azul = '\033[1;34m'
azul_c = '\033[1;36m'


def lin(tam = 60):
    return f'*' * tam


def lin2(msg, tam = 60):
    return f'{azul}{msg.center(tam).replace(' ', '*')}{s_cor}'


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print(f'{vermelho}Erro! Digite um número válido!{s_cor}')
        else:
            break
    return num


def cabeçalho(msg):
    print(lin())
    print(f'{azul}{msg.center(60)}{s_cor}')
    print(lin())

def data():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    dt = f'{dia}/{mes}/{ano}'
    if dia < 10 and mes < 10:
        dt = f'0{dia}/0{mes}/{ano}'
    elif dia < 10:
        dt = f'0{dia}/{mes}/{ano}'
    elif mes < 10:
        dt = f'{dia}/0{mes}/{ano}'
    msg = 'Data'
    print(f'{azul}{msg:^30}{dt:^30}{s_cor}')


def menu():
    cabeçalho('Estacionamento "Aí Dentu"')
    data()
    opc = ['Entrada', 'Saída', 'Pátio', 'Histórico Saída','Configurar','Fechar Sistema']

    print(f'{lin2('||MENU||')}')
    for c, i in enumerate (opc):
        print(f' [ {vermelho}{c + 1 if not c == 5 else 0}{s_cor} ] - {azul_c}{i}{s_cor}')
    print(f'{azul}{lin()}{s_cor}')
    

def escolha():
    cond = leiaint('Digite: ')
    while cond < 0 or cond > 5:
        print(f'{vermelho}Erro! Opção inexistente, tente novamente.{s_cor}')
        cond = leiaint('Digite: ')
    return cond



def configurar_preço(atual, tolerancia):
    system('clear')
    cabeçalho('PREÇO')
    print(f'{ng}Valor {atual} reias a hora')
    print(f'Tolerância {tolerancia:.0f} minutos{s_cor}')
    print(lin())
    print(f' [{vermelho} 1{s_cor} ] -{azul_c} Alterar{s_cor}\n [{vermelho} 2{s_cor} ] - {azul_c}Voltar{s_cor}')
    print(lin())
    cond = leiaint('Digite: ')
    while cond < 1 or cond > 2:
        print(f'{vermelho}Erro! Opção inxistente, tente novamente.{s_cor}')
        cond = leiaint('Digite: ')
    print(lin())
    if cond == 1:
        n1 = leiaint('Novo preço: R$ ')
        n2 = leiaint('Nova tolerância: ')
        return [n1, n2]
    else:
        return False

def leia_placa(msg):
    while True:
        antigo = r'[A-Z]{3}[0-9]{4}$'
        novo = r'[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}$'
        plc = str(input(msg)).upper().strip().replace(' ', '').replace('-', '')
        if re.match(antigo, plc) or re.match(novo, plc):
            break
        else:
            print(f'{vermelho}Formato de placa inválido. Tente novamente.{s_cor}')
    return plc

def doc_cal_saida(dado_dic_saida):
    # Extrair o horário de entrada do dicionário
    hora_entrada = dado_dic_saida['HoraEnt']

    # Obter o horário atual (momento da saída)
    hora_saida = datetime.now()

    # Calcular a diferença de tempo entre entrada e saída
    tempo_total = hora_saida - hora_entrada
    minutos_total = tempo_total.total_seconds() / 60  # converter para minutos

    # Extrair valores da lista tole_valor
    valor_por_hora = dado_dic_saida['ValorBase'][0]
    tolerancia = dado_dic_saida['ValorBase'][1]

    

    # Calcular a quantidade total de horas (arredondando para cima para cobrança)
    horas_cobradas = ceil(minutos_total / 60)
    valor_a_pagar = horas_cobradas * valor_por_hora

    # Calcular horas e minutos para exibir no formato hh:mm
    horas = int(minutos_total // 60)
    minutos = int(minutos_total % 60)
    tempo_formatado = f"{horas:02}:{minutos:02}"

    # Se o tempo total for menor ou igual à tolerância, o valor é zero
    if minutos_total <= tolerancia:
        return [0.0, tempo_formatado, 'isento de tarifa']

    return [valor_a_pagar, tempo_formatado]

def console(*dado):
    print(lin())
    for i in dado:
        print(i)
    print(lin())
