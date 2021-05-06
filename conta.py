class Conta:
    def __init__(self, titular, numero, saldo=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError('Valor a ser sacado excede o saldo atual')
        self.saldo -= valor
    
    def __str__(self):
        descricao = f'Titular: {self.titular}, Número: {self.numero},'
        descricao += f' Saldo: {self.saldo}'
        return descricao


class Poupanca(Conta):
    def aplicar_juros(self):
        self.saldo = self.saldo * 1.0005
    
    def depositar(self, valor):
        self.aplicar_juros()
        super().depositar(valor)

    def sacar(self, valor):
        self.aplicar_juros()
        super().sacar(valor)

