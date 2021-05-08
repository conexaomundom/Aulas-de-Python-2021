# Todos os servicos
from conta import Conta, Poupanca
from EditandoValor import change_string_in_file

agencia = {
    'contas correntes': [],
    'poupanças': []
}

while True:
    print('Serviços disponíveis no momento: ')
    print(' Abrir Conta \n Deposito \n Saque \n Fechar conta \n')
    print('Para sair: stop  \n')
        
    servico = input('Qual tipo de serviço deseja? ')
    # Estava dando problema na avaliacao do if quando
    # colocava o .lower() na mesma linha do input
    servico = servico.lower()
    if servico == 'stop':
        break
    titular = input('Digite o nome do titular: ').lower()
    numero = input('Digite o número da conta: ')
    tipo = input('Qual o tipo de conta: \n Conta \n Poupanca ')
    
    titular = titular.lower()
    tipo = tipo.lower()
    
    dados = str('Titular: {}, Número: {}'.format(titular,numero))
    print(servico.split())
    filename = 'agencia.txt'
    
    if servico == 'deposito' or servico == 'saque':
        if servico == 'deposito':
            valor = float(input('Qual valor gostaria de depositar: '))
        elif servico == 'saque':
            valor = float(input('Qual valor gostaria de sacar: '))

        change_string_in_file(filename = 'agencia.txt', string_to_search = string_to_search, servico = servico, valor = valor)

    if servico == 'fechar':
        with open ('agencia.txt', 'r') as read_obj:
            for line in read_obj:
                if dados in line:
                    old_string = line

                    f = open(filename, 'r')
                    filedata = f.read()
                    f.close()

                    newdata = filedata.replace(old_string, '\n')

                    f = open(filename, 'w')
                    f.write(newdata)
                    f.close()
                    
                    print(newdata)
    else:
        saldo_inicial = float(input('Qual o valor de deposito inicial: '))
        if tipo == 'conta':
            c = Conta(titular, numero, saldo_inicial)
            agencia['contas correntes'].append(c)
        elif tipo == 'poupanca':
            c = Poupanca(titular, numero, saldo_inicial)
            agencia['poupanças'].append(c)
        else:
            raise ValueError('Tipo de conta desconhecido')
        print('Salvando arquivo')

        with open('agencia.txt', 'w') as arquivo:
            for tipo_de_conta in agencia:
                for conta in agencia[tipo_de_conta]:
                    arquivo.write(str(conta))
        print('Arquivo salvo')
print(dados)
