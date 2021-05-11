# Todos os servicos
#from conta import Conta, Poupanca
from main5 import Agencia
import os

extrato = { }


while True:
    print('\n \n \n')
    print('Serviços disponíveis no momento: ')
    print(' Abrir Conta \n Deposito \n Saque \n Fechar conta \n')
    print('Para sair: stop  \n')
    
    servico = input('Qual tipo de serviço deseja? \n')
    # Estava dando problema na avaliacao do if quando
    # colocava o .lower() na mesma linha do input
    servico = servico.lower()
    # print(servico.split())

    # sair do terminal
    if servico == 'stop':
       break
    
    print('\n \n \n')
    agencia_n = str(input('Digite o numero da sua agencia: '))
    numero = input('Digite o número da conta: ')
    titular = input('Digite o nome do titular: ').lower()
    tipo = input('Qual o tipo de conta: \n Conta \n Poupanca \n').lower()
    print('\n \n \n')
    
    #
    filename = agencia_n + '.txt'
    c = Agencia(titular, numero, tipo)
    dados = str('Titular: {}, Número: {}'.format(titular,numero))
    
    if servico == 'deposito' or servico == 'saque':
        
        if not '{}_{}_{}_deposito'.format(agencia_n, titular,numero) in list(extrato.keys()):
            extrato['{}_{}_{}_deposito'.format(agencia_n, titular,numero)] = []
        if not '{}_{}_{}_saque'.format(agencia_n, titular,numero) in list(extrato.keys()):
            extrato['{}_{}_{}_saque'.format(agencia_n, titular,numero)] = []
        
        if servico == 'deposito':
            valor = float(input('Qual valor gostaria de depositar: '))
            
        elif servico == 'saque':
            valor = float(input('Qual valor gostaria de sacar: '))

        c.change_string_in_file(filename = filename, string_to_search = dados, servico = servico, valor = valor)
        extrato['{}_{}_{}_{}'.format(agencia_n, titular,numero,servico)].append(valor)

    # imprimir extrato da conta
    elif servico == 'extrato':
        c.imprimir_extrato(extrato, dados, agencia_n)

    # fechar conta
    elif servico == 'fechar':
        Agencia(titular, numero, tipo).fechar(filename)

    # abrir conta
    elif servico == 'abrir':
        
        saldo_inicial = input('Qual o valor de deposito inicial: ')
        criar_agencia = float(input('Deseja criar uma agencia: 0-não 1-sim \n'))
        print('\n \n \n')
        
        while True:

            try:
                if ',' in saldo_inicial:
                    #print('Valor inválido, virgula no lugar do ponto')
                    saldo_inicial = saldo_inicial.replace(',','.')
                    saldo_inicial = float(saldo_inicial)
                    #print((saldo_inicial > 0))
                    if float == type(saldo_inicial) and saldo_inicial > 0:
                        break
                    
                if float(saldo_inicial) < 0:
                    #print('Valor inválido, valor negativo foi inserido')
                    saldo_inicial = input('Qual o valor de deposito inicial: ')
                    saldo_inicial = float(saldo_inicial)
                    if float == type(saldo_inicial) and saldo_inicial > 0:
                        break

                if float == type(float(saldo_inicial)) and float(saldo_inicial) > 0:
                    saldo_inicial = float(saldo_inicial)
                    break
                
            except:
                print('Valor inválido')
                saldo_inicial = input('Qual o valor de deposito inicial: ')
                    #saldo_inicial = float(saldo_inicial)   
        

        if criar_agencia == 1:
            Agencia(titular, numero, tipo, saldo_inicial).criar(filename)
            #print(a)
        # Conta já existente
        else:
            Agencia(titular, numero, tipo, saldo_inicial).existente(filename)
            
    else:
        print(ValueError('Esta operação não está disponível no momento \n'))
        continue

diretorio = str(input('Digite qual diretório se encontra esse arquivo: \n'))
print(os.listdir(diretorio))  
print('Usuário desejou sair do terminal')
