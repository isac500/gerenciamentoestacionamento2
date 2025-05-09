from ast import literal_eval
def arq_existe (arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def cria_arquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo!')

def registrar_dados(arq, dado_saida):
    global aa
    try:
        aa = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            aa.write(f'{dado_saida}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        
    finally:
        aa.close()

def ler_arquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        for i in a:
            i = literal_eval(i)
            print(f'{i['DataEnt']:^11}{i['HoraEnt']:^6}{i['Placa']:^10}{i['Modelo']:^12}pago: {i['Valor']:<7}Permanência: {i['Permanência']}')
    finally: 
        a.close()
