# Todos os servicos
from conta import Conta, Poupanca
from EditandoValor import change_string_in_file

agencia = {
    'contas correntes': [],
    'poupanças': []
}

while True:
    servico = input('Qual tipo de serviço o(a) senhor(a) deseja:  \n Abrir \n Deposito \n Saque \n Fechar \n').lower()
    if servico == 'stop':
        break
    tem_conta = input('O(a) Senhor(a) já tem conta? (1) p/ Sim ou (2) p/ Nao')
    titular = input('Digite o nome do(a) titular: ')
    numero = input('Digite o número da conta: ')
    tipo = input('Digite o tipo da conta: ').lower()
    try:

        if servico == 'deposito' or servico == 'saque':
            valor = float(input('Qual valor? '))
            string_to_search = str('Titular: {}, Número: {}'.format(titular,numero))
            change_string_in_file(filename = 'agencia.txt', string_to_search = string_to_search, servico = servico, valor = valor)
            
        elif servico == 'fechar':
            dados = str('Titular: {}, Número: {}'.format(titular,numero))
            with open('agencia.txt', 'r') as read_obj:
                    # Read all lines in the file one by one
                for line in read_obj:
                        # For each line, check if line contains the string
                    if dados in line:
                        old_string = line
                             
                        f = open(filename, 'r')
                        filedata = f.read()
                        f.close()

                        newdata = filedata.replace(old_string, '\n')

                        f = open(filename, 'w')
                        f.write(newdata)
                        f.close()
            

        else:
            saldo_inicial = float(input('Digite o saldo inicial: '))
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
                    arquivo.write(tipo_de_conta + '\n')
                    for conta in agencia[tipo_de_conta]:
                        arquivo.write(str(conta))
                        arquivo.write('\n')
                    arquivo.write('#########################################')
                    arquivo.write('\n')

print('Arquivo salvo')
