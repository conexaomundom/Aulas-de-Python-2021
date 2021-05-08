
from EditandoValor import change_string_in_file

agencia = {
    'contas correntes': [],
    'poupanças': []
}

while True:
    print('Serviços disponíveis no momento: ')
    print(' Abrir Conta \n Deposito \n Saque \n Fechar conta \n')
    print('Para sair: stop  \n')
        
    servico = input('Qual tipo de serviço deseja? ').lower()
    # Estava dando problema na avaliacao do if quando
    # colocava o .lower() na mesma linha do input
    # servico = servico.lower()
    if servico == 'stop':
        break
    titular = input('Digite o nome do titular: ').lower()
    numero = input('Digite o número da conta: ')
    tipo = input('Qual o tipo de conta: \n Conta \n Poupanca ').lower()
    
    dados = str('Titular: {}, Número: {}'.format(titular,numero))
    print(servico.split())
    filename = 'agencia.txt'
    saldo_inicial = float(input('Qual o valor de deposito inicial: '))
    c = str(' \nTitular: {}, Número: {}, Saldo: {}'.format(titular, numero, saldo_inicial))
    if tipo == 'conta':
        tipo_de_conta = 'contas correntes'
    elif tipo == 'poupanca':
        tipo_de_conta = 'poupancas'
    else:
        raise ValueError('Tipo de conta desconhecido')
        print()
        
    print(tipo_de_conta)
    
    with open ('agencia.txt', 'r') as read_obj:
        for line in read_obj:
            if tipo_de_conta in line:
                print(tipo_de_conta)
