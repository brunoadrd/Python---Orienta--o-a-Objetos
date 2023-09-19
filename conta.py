class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    
    def depositar(self, valor):
        self.__saldo += valor

    def __limiteDisponivel(self, valor):
        return (valor <= self.__saldo + self.__limite)
    
    def sacar(self, valor):
        if (self.__limiteDisponivel(valor)):
            self.__saldo -= valor
        else: 
            print(f'O saque de {valor} excedeu o limite')

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @property
    def extrato(self):
        print(f'O saldo do titular {self.__titular} é de: R$ {self.__saldo}')

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @staticmethod
    def codigo_banco():
        return "001"