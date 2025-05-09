from gerenciamentoestacionamento2.0.ai_dentu.interface import *
from gerenciamentoestacionamento2.0.ai_dentu.lib import *
from datetime import date, datetime

arq_saida = 'relatorio_saida.txt'

if not arq_existe(arq_saida):
    cria_arquivo(arq_saida)
    print('Arquivo criado com sucesso!')

patio = []
patio_ent = {}
patio_sai = {}
preço_tolerancia = [5, 20]
system('clear')
menu()
while True:
    totpatio = 0
    res = escolha()

    if res == 1:
        system ('clear')
        cabeçalho('[ 1 ] - Entrada')
        validar_placa = str(leia_placa('Placa: '))
        validar = True
        for i in patio:
            if i['Placa'] == validar_placa:
                system('clear')
                menu()
                console('Este veículo já está no pátio.')
                validar = False
                break
        if validar:
            patio_ent['ValorBase'] = preço_tolerancia.copy()
            patio_ent['Placa'] = validar_placa
            patio_ent['Modelo'] = str(input('Modelo: ')).upper().strip()
            patio_ent['HoraEnt'] = datetime.now()
            patio_ent['DataEnt'] = datetime.now().strftime('%d/%m/%Y')
            patio.append(patio_ent.copy())
            system('clear')
            menu()
            console(f'{patio_ent['Modelo']} {patio_ent['Placa']} entrada efetuada com sucesso!')
            
        
    elif res == 2:
        system('clear')
        cabeçalho('[ 2 ] - Saída')
        validar_placa = leia_placa('Placa: ')
        validar = False
        for i in patio:
            if i['Placa'] == validar_placa:
                system('clear')
                cabeçalho('[ 2 ] - Saída')
                validar = True
                doc_saida = doc_cal_saida(i)
                print(f'{'Placa:':<20} {i['Placa']}')
                hora_format = i['HoraEnt'].strftime('%H:%M')
                print(f'{'Entrada:':<20} {i['DataEnt']} Hora: {hora_format}')
                print(f'{'Saída:':<20} {datetime.now().strftime('%d/%m/%Y')} Hora: {datetime.now().strftime('%H:%M')}')
                if len(doc_saida) == 3:
                    print(f'{'Permanência:':<20} {doc_saida[1]}\n{'Total a ser pago:':<20} {doc_saida[0]:.2f} {doc_saida[2]}')
                else:
                    print(f'{'Permanência:':<20} {doc_saida[1]}\n{'Total a ser pago:':<20} {doc_saida[0]:.2f}')
                print(lin())
                cond_saida = str(input('"ENTER" para confirmar pagamento ("999" para cancelar): ')).strip()
                while cond_saida != '' and cond_saida != '999':
                    print('\033[31mExpressão inválida\033[m')
                    cond_saida = str(input('"ENTER" para confirmar pagamento ("999" para cancelar): '))
                if cond_saida == '':
                    i['HoraEnt'] = i['HoraEnt'].strftime('%H:%M')
                    i['Valor'] = f'{doc_saida[0]:.2f}'
                    i['Permanência'] = doc_saida[1]
                    registrar_dados(arq_saida, i)
                    patio.remove(i)
                    system('clear')
                    menu()
                    console(f'Saída do veículo {validar_placa} registrado com sucesso!')
                else:
                    system('clear')
                    menu()
                    console(f'Saída cancelada!')
                break
        if not validar:
            system('clear')
            menu()
            console('Este veículo não se encontra no pátio')


    elif res == 3:
        system('clear')
        cabeçalho('[ 3 ] - Pátio')
        for i in patio:
            print(f'{i['DataEnt']:^11}{i['HoraEnt'].strftime('%H:%M'):^6}{i['Placa']:^12}{i['Modelo']:^16}')
            totpatio += 1
        if totpatio == 0:
            print('\033[1mNão há veículos no pátio.\033[m')
        else:
            print(f'\033[1mTotal veículos no pátio: {totpatio}\033[m')
        print(lin())
        menu()

    elif res == 4:
        system('clear')
        cabeçalho('[ 4 ] - Histórico de Saída')
        ler_arquivo(arq_saida)
        menu()
    elif res == 5:
        system('clear')
        while True:
            resc = configurar_preço(preço_tolerancia[0], preço_tolerancia[1])
            if resc is False:
                break
            else:
                preço_tolerancia[0] = resc[0]
                preço_tolerancia[1] = resc[1]
        system('clear')
        menu()
    else:
        cabeçalho('Encerrado!')
        break
