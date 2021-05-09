# Todos os servicos
from conta import Conta, Poupanca
from EditandoValor import change_string_in_file


while True:
    print('Serviços disponíveis no momento: ')
    print(' Abrir Conta \n Deposito \n Saque \n Fechar conta \n')
    print('Para sair: stop  \n')
        
    servico = input('Qual tipo de serviço deseja? ')
    # Estava dando problema na avaliacao do if quando
    # colocava o .lower() na mesma linha do input
    servico = servico.lower()
    # print(servico.split())
    
    if servico == 'stop':
       break
 
    titular = input('Digite o nome do titular: ').lower()
    numero = input('Digite o número da conta: ')
    tipo = input('Qual o tipo de conta: \n Conta \n Poupanca ').lower()
    
    dados = str('Titular: {}, Número: {}'.format(titular,numero))
    # print(servico.split())
    filename = 'agencia.txt'
    
    if servico == 'deposito' or servico == 'saque':
        if servico == 'deposito':
            valor = float(input('Qual valor gostaria de depositar: '))
        elif servico == 'saque':
            valor = float(input('Qual valor gostaria de sacar: '))

        change_string_in_file(filename = 'agencia.txt', string_to_search = dados, servico = servico, valor = valor)

    elif servico == 'fechar':
        with open ('agencia.txt', 'r') as read_obj:
            for line in read_obj:
                if dados in line:
                    old_string = line

                    f = open(filename, 'r')
                    filedata = f.read()
                    f.close()

                    newdata = filedata.replace(old_string, '')
                    
                    print('Salvando arquivo \n')
                    print(newdata + '\n')
                    f = open(filename, 'w')
                    f.write(newdata)
                    f.close()
                    print(newdata + '\n')
                else:
                    print(ValueError('Conta não encontrada nessa agência, tente novamente '))
                    continue
                    
    elif servico == 'abrir':
        saldo_inicial = input('Qual o valor de deposito inicial: ')
        
        #if saldo_inicial > 1:
         #   print('Valor inválido para saldo inicial, digite valor único')
          #  continue
        while True:
           
            try:
                if ',' in saldo_inicial:
                    print('Valor inválido, virgula no lugar do ponto')
                    saldo_inicial = saldo_inicial.replace(',','.')
                    print('1111')
                    saldo_inicial = float(saldo_inicial)
                    print((saldo_inicial > 0))
                    if float == type(saldo_inicial) and saldo_inicial > 0:
                        print('4444')
                        break
                    
                if float(saldo_inicial) < 0:
                    print('3333')
                    print('Valor inválido, valor negativo foi inserido')
                    saldo_inicial = input('Qual o valor de deposito inicial: ')
                    saldo_inicial = float(saldo_inicial)
                    if float == type(saldo_inicial) and saldo_inicial > 0:
                        break
                
            except:
                if float == type(saldo_inicial):
                    if saldo_inicial > 0:
                        break
                else:
                    print('Valor inválido')
                    saldo_inicial = input('Qual o valor de deposito inicial: ')
                    #saldo_inicial = float(saldo_inicial)
    
        
        saldo_inicial == float(saldo_inicial)
        c = str(' \nTitular: {}, Número: {}, Saldo: {}'.format(titular, numero, saldo_inicial))

        if tipo == 'conta':
            tipo_de_conta = 'contas correntes'
        elif tipo == 'poupanca':
            tipo_de_conta = 'poupanças'
        else:
            raise ValueError('Tipo de conta desconhecido')
            print()
        print('Salvando arquivo')
        with open ('agencia.txt', 'r') as read_obj:
            for line in read_obj:
                if tipo_de_conta in line:
                    old_string = tipo_de_conta
                    f = open(filename, 'r')
                    filedata = f.read()
                    f.close()
                    
                    new_string = old_string + c

                    newdata = filedata.replace(old_string, new_string)
                    # print(newdata + '\n')
                    print('Salvando nova conta')
                    f = open(filename, 'w')
                    f.write(newdata)
                    f.close()
                    
                    print(new_string)
        #print(new_string)
    else:
        print(ValueError('Esta operação não está disponível no momento \n'))
        continue
        
print('Usuário desejou sair do terminal')
