# Todos os servicos
# from EditandoValor import change_string_in_file
import os

class Conta:
    def __init__(self, titular, numero, tipo, saldo_inicial=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo_inicial = saldo_inicial
        self.tipo = tipo


        
    def imprimir_extrato(self, extrato, dados, agencia_n):

        dep = []

        for i in extrato['{}_{}_{}_deposito'.format(agencia_n,self.titular, self.numero)]:
            dep.append('Deposito: {} \n'.format(i))   
        
        for j in extrato['{}_{}_{}_saque'.format(agencia_n,self.titular, self.numero)]:
            dep.append('Saque: {} \n'.format(j))

        for k in dep:
            texto = 'Agencia: {} \n'.format(agencia_n)
            texto += '{}\n'.format(self.tipo)
            texto += dados + '\n'
                               
            texto += k
            print(texto)

  
    def depositar(self, valor):
        self.saldo_inicial += valor
        #self.extrato['deposito'].apeend(valor)
        

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError('Valor a ser sacado excede o saldo atual')
        self.saldo_inicial -= valor
        #self.extrato['saque'].apeend(valor)

    def extrato(self):
        print(self.extrato)
    
    def __str__(self):
        descricao = f'Titular: {self.titular}, Número: {self.numero},'
        descricao += f' Saldo: {self.saldo_inicial}'
        return descricao
    
class Poupanca(Conta):
    def aplicar_juros(self):
        self.saldo_inicial = self.saldo_inicial * 1.0005
    
    def depositar(self, valor):
        self.aplicar_juros()
        super().depositar(valor)

    def sacar(self, valor):
        self.aplicar_juros()
        super().sacar(valor)


class Agencia(Conta):

    def criar(self, filename):
        agencia = {
            'contas correntes': [],
            'poupanças': []
        }
        try:
            if self.tipo == 'conta':
                c = Conta(self.titular, self.numero, self.saldo_inicial)
                agencia['contas correntes'].append(c)
            elif self.tipo == 'poupanca':
                c = Poupanca(self.titular, self.numero, self.saldo_inicial)
                agencia['poupanças'].append(c)
            else:
                raise ValueError('Tipo de conta desconhecido')
            print()
        except ValueError:
            print('Usuário tentou cadastrar tipo de conta desconhecido')
        
        with open(filename, 'w') as arquivo:
                for tipo_de_conta in agencia:
                    arquivo.write(tipo_de_conta + '\n')
                    for conta in agencia[tipo_de_conta]:
                        arquivo.write(str(conta))
                        arquivo.write('\n')
                    arquivo.write('#########################################')
                    arquivo.write('\n')

        print('Arquivo salvo')

    def existente(self, filename):

        c = Conta(self.titular, self.numero, self.tipo, self.saldo_inicial)
        
        if self.tipo == 'conta':
            tipo_de_conta = 'contas correntes'
        elif self.tipo == 'poupanca':
            tipo_de_conta = 'poupanças'
        else:
            raise ValueError('Tipo de conta desconhecido')
        
        with open (filename, 'r') as read_obj:
            for line in read_obj:
                if tipo_de_conta in line:
                    old_string = tipo_de_conta
                    f = open(filename, 'r')
                    filedata = f.read()
                    f.close()
                        
                    new_string = old_string + '\n' + str(c)

                    newdata = filedata.replace(old_string, new_string)
                    # print(newdata + '\n')
                    print('Salvando nova conta')
                    f = open(filename, 'w')
                    f.write(newdata)
                    f.close()
                        
        print(new_string)

    def fechar(self, filename):

        dados = str('Titular: {}, Número: {}'.format(self.titular,self.numero))
        
        with open (filename, 'r') as read_obj:
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

    def change_string_in_file(self, filename, string_to_search, servico, valor):
        
    #""" Check if any line in the file contains given string """
    # Open the file in read only mode
        with open(filename, 'r') as read_obj:
            # Read all lines in the file one by one
            for line in read_obj:
                # For each line, check if line contains the string
                if string_to_search in line:
                    old_string = line
                    linha = line.split()
                    old_saldo = float(linha[-1])
                    
                    if servico == 'deposito':
                        novo_saldo = old_saldo + valor
                        
                    elif servico == 'saque':
                        if valor > old_saldo:
                            raise ValueError('Valor a ser sacado excede o saldo atual')
                        novo_saldo = old_saldo - valor
                        
                    linha[-1] = str(novo_saldo)
                    new_string = ' '.join(linha) + ' \n'
                    #new_string = new_string + ' \n'


                    f = open(filename, 'r')
                    filedata = f.read()
                    f.close()

                    newdata = filedata.replace(old_string, new_string)

                    f = open(filename, 'w')
                    f.write(newdata)
                    f.close()
                    
                    return  print(newdata)
        return ValueError('Esta conta não está cadastrada no banco')


    def todas_agencias(diretorio):
        os.listdir(diretorio)
        for i in diretorio:
            f = open(i, 'r')
            filedata = f.read()
            f.close()
            print(filedata)

            



            
    
