import cliente
import transacao


class Conta():
    _agencia = '0001'

    def get_saldo(self):
        return self._saldo
    
    def get_numero(self):
        return self._numero
    
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero
        self._saldo = 0.0
        historico = transacao.Historico()
        self._historico = historico

    def sacar(self, valor):
        inicia_transacao = transacao.Saque()
        saque = inicia_transacao.validar(self, valor)
        if saque == True:
            self._saldo = self._saldo - valor 
            inicia_transacao.registrar(self)
            return True
        else:
            return False


    def depositar(self, valor):
        inicia_transacao = transacao.Deposito()
        deposito = inicia_transacao.validar(self, valor)
        if deposito == True:
            self._saldo = self._saldo + valor 
            inicia_transacao.registrar(self)
            return True
        else:
            return False
        
    def consultar_extrato(self):
        print(f"Saldo atual da conta: R${self._saldo:.2f}.\nOperações anteriores:\n")
        return self._historico._extrato
    
    def get_historico(self):
        return self._historico
        

class ContaCorrente(Conta):
    _limite = 500
    _limite_saques = 3

    def get_limite(self):
        return self._limite
    
    def set_limite(self, limite):
        self._limite = limite

    def get_limite_saques(self):
        return self._limite_saques
    
    def set_limite_saques(self, limite_saques):
        self._limite_saques = limite_saques