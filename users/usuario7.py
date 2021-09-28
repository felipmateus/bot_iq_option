import sys
from iqoptionapi.stable_api import IQ_Option

email = sys.argv[1]
senha = sys.argv[2]
tipo = sys.argv[11]

API = IQ_Option(email, senha)
API.connect()
API.change_balance(tipo)

if API.check_connect():
    print('Conectado com sucesso! ')
else:
    print('Erro ao se conectar! ')
    input('\n\n Aperte enter para sair')
    sys.exit()

while True:
    comprar_digital = open('comprar_digital.txt', 'r').read()
    comprar_binario = open('comprar_binario.txt', 'r').read()
    stop = open('stop.txt', 'r').read()
    if stop == 'True':
        sys.exit()

    if comprar_digital == "True":

        dinheiro_dig = sys.argv[7]
        moeda_dig = sys.argv[9]
        acao_dig = sys.argv[8]
        tempo_dig = sys.argv[10]

        status_d, id_d = API.buy_digital_spot(moeda_dig, int(dinheiro_dig), acao_dig, int(tempo_dig))
        if status_d:
            print(f"Operação digital comprada com sucesso! \n ID: {id_d}")
        # print('Compra em digital: ', status_d, id_d)
        g = open('comprar_digital.txt', 'w')
        g.write('False')

        while True:
            f = open('digital.txt', 'r')
            letra = f.read()
            if letra == "True":
                break

        # print('Vendendo digital: ', end='')
        status = API.close_digital_option(id_d)
        if status:
            print(f"Operação digital vendida com sucesso. \n ID: {id_d}")
        else:
            print('Erro ao vender operação')

    if comprar_binario == "True":

        dinheiro_bin = int(sys.argv[3])
        moeda_bin = sys.argv[4]
        acao_bin = sys.argv[5]
        tempo_bin = int(sys.argv[6])

        status_b, id_b = API.buy(dinheiro_bin, moeda_bin, acao_bin, tempo_bin)
        # status_b, id_b = API.buy(2, 'EURUSD', 'put', 1)
        if status_b:
            print(f"Operação binária comprada com sucesso. \n ID: {id_b}")
        # print('Compra em binário: ', status_b, id_b)
        g = open('comprar_binario.txt', 'w').write('False')

        while True:
            f = open('binario.txt', 'r')
            letra = f.read()
            if letra == "True":
                break

        # print('Vendendo binária: ', end='')
        # print(type(id_b))
        status = API.sell_option(id_b)
        # print(status)
        if 'error' in status['msg'][str(id_b)]:
        # if status:
            print('Erro ao vender operação binária')
        else:
            print(f"Operação binária vendida com sucesso  \n ID: {id_b}")