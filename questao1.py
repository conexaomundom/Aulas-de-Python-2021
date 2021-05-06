from conta import Conta, Poupanca


agencia = {
    'contas correntes': [],
    'poupanças': []
}

while True:
    print('Os serviços disponíveis são: \n Criar Conta \n ')
    print('Deposito \n Saque \n Fechar Conta')
    servico = input('Qual serviço o(a) senhor(a) gostaria de solicitar: ')


    titular = input('Digite o nome do(a) titular: ')
    if titular == 'stop':
        break
    numero = input('Digite o número da conta: ')
    saldo_inicial = float(input('Digite o saldo inicial: '))
    tipo = input('Digite o tipo da conta: ').lower()
    try:
        if tipo == 'conta':
            c = Conta(titular, numero, saldo_inicial)
            agencia['contas correntes'].append(c)
        elif tipo == 'poupanca':
            c = Poupanca(titular, numero, saldo_inicial)
            agencia['poupanças'].append(c)
        else:
            raise ValueError('Tipo de conta desconhecido')
        print()
    except ValueError:
        print('Usuário tentou cadastrar tipo de conta desconhecido')

    if servico == "criar conta":
        print('Salvando arquivo')

        with open('agencia.txt', 'w') as arquivo:
            for tipo_de_conta in agencia:
                arquivo.write(tipo_de_conta + '\n')
                for conta in agencia[tipo_de_conta]:
                    arquivo.write(str(conta))
                    arquivo.write('\n')
                arquivo.write('#########################################')
                arquivo.write('\n')

        print('Arquivo salvo')

    if servico == 'deposito'
        if tipo == 'conta'
           with open('agencia.txt', 'w'):
                for tipo_de_conta in agencia:
                arquivo.write(tipo_de_conta + '\n')
                for conta in agencia[tipo_de_conta]:
                    arquivo.write(str(conta))
                    arquivo.write('\n')
                arquivo.write('#########################################')
                arquivo.write('\n')
            
