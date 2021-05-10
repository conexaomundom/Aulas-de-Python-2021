def __init__(self, titular, numero, saldo_inicial=0.0):
    self.titular = titular
    self.numero = numero
    self.saldo_inicial = saldo_inicial
    while True:

        try:
            if ',' in self.saldo_inicial:
                print('Valor inválido, virgula no lugar do ponto')
                self.saldo_inicial = self.saldo_inicial.replace(',','.')
                self.saldo_inicial = float(self.saldo_inicial)
                print((self.saldo_inicial > 0))
                if float == type(self.saldo_inicial) and self.saldo_inicial > 0:
                    break
                    
            if float(self.saldo_inicial) < 0:
                print('Valor inválido, valor negativo foi inserido')
                self.saldo_inicial = input('Qual o valor de deposito inicial: ')
                self.saldo_inicial = float(self.saldo_inicial)
                if float == type(self.saldo_inicial) and self.saldo_inicial > 0:
                    break

            if float == type(float(self.saldo_inicial)) and float(self.saldo_inicial) > 0:
                self.saldo_inicial = float(self.saldo_inicial)
                break
                
        except:
            print('Valor inválido')
            self.saldo_inicial = input('Qual o valor de deposito inicial: ')
            #saldo_inicial = float(saldo_inicial)   
