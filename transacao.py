from abc import ABC
import conta

LIMITE_SAQUES = 3

class Transacao(ABC):
    def registrar(self, conta):
        conta.get_historico().adicionar_transacao(self)



class Deposito(Transacao):

    def __init__(self):
        self._valor = 0.0

    def validar(self, conta, valor):
        self._conta = conta
        self._valor = valor
        if valor < 0:
            print("Impossível fazer depósito negativo.")
            return False
        else: 
            print("Depósito realizado com sucesso.")
            return True
        
    def get_valor(self):
        return self._valor


class Saque(Transacao):

    def __init__(self):
        self._valor = 0.0

    def validar(self, conta, valor):
        self._conta = conta
        self._valor = valor
        if conta.get_limite_saques() > 3:
            print("Erro: número de saques diário excedido.")
            return False
        else:
            if conta.get_saldo() - self._valor < 0:
                print("Impossível realizar este saque: saldo insuficiente.")
                return False
            elif self._valor > conta.get_limite():
                print("Impossível realizar este saque: limite para saques excedido.")
                return False
            else: 
                x = conta.get_limite_saques() + 1
                conta._set_limite_saques(x)
                print("Saque realizado com sucesso.")
                return True
            
    def get_valor(self):
        return self._valor


class Historico():
    def __init__(self):
        self._extrato = ""

    def adicionar_transacao(self, transacao):
        if isinstance(transacao, Deposito):
            self._extrato = self._extrato + f"Depósito de {transacao.get_valor()} reais. \n"
        if isinstance(transacao, Saque):
            self._extrato = self._extrato + f"Saque de {transacao.get_valor()} reais. \n"


        