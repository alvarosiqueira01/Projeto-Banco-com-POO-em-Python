from abc import ABC
import conta
from datetime import datetime

LIMITE_SAQUES = 3

class Transacao(ABC):
    def registrar(self, conta):
        conta.get_historico().adicionar_transacao(self)



class Deposito(Transacao):

    def __init__(self):
        self._valor = 0.0
        self.data_e_hora = datetime.now()

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
    
    def get_data_e_hora(self):
        return self.data_e_hora
    


class Saque(Transacao):

    def __init__(self):
        self._valor = 0.0
        self.data_e_hora = datetime.now()

    def validar(self, conta, valor):
        self._conta = conta
        self._valor = valor
        if conta.get_limite_saques() > LIMITE_SAQUES:
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
                conta.set_limite_saques(x)
                print("Saque realizado com sucesso.")
                return True
            
    def get_valor(self):
        return self._valor
    
    def get_data_e_hora(self):
        return self.data_e_hora


class Historico():
    def __init__(self):
        self._extrato = ""
        self._n_de_depositos = 0
        self._n_de_saques = 0

    def adicionar_transacao(self, transacao):
        if isinstance(transacao, Deposito):
            self._extrato = self._extrato + f"Depósito de {transacao.get_valor()} reais realizado em {transacao.get_data_e_hora()} \n"
            self._n_de_depositos += 1
        if isinstance(transacao, Saque):
            self._extrato = self._extrato + f"Saque de {transacao.get_valor()} reais realizado em {transacao.get_data_e_hora()} \n"
            self._n_de_saques += 1

    def gerar_relatorio(self, transacao=None):

        if not transacao:

            linhas_extrato = []
            numero_linha = 0
            indice = 0
            indices_onde_a_linha_quebra = []
            for char in self._extrato:
                indice += 1
                if char == "\n":
                    indices_onde_a_linha_quebra.append(indice)
                    numero_linha += 1
                    for i in range(indices_onde_a_linha_quebra[indice-1],indices_onde_a_linha_quebra[indice]):
                        linhas_extrato[numero_linha].append(self._extrato[i])

                    yield linhas_extrato[numero_linha]

        else: 

            if isinstance(transacao, Deposito):
                
                linhas_extrato = []
                numero_linha = 0
                indice = 0
                indices_onde_a_linha_quebra = []
                for char in self._extrato:
                    indice += 1
                    if char == "\n":
                        indices_onde_a_linha_quebra.append(indice)
                        numero_linha += 1
                        for i in range(indices_onde_a_linha_quebra[indice-1],indices_onde_a_linha_quebra[indice]):
                            linhas_extrato[numero_linha].append(self._extrato[i])

                        substring = "Depósito"
                        string = linhas_extrato[numero_linha]
                        isin = (substring in string)
                        if isin == True:
                            yield string

            if isinstance(transacao, Saque):

                linhas_extrato = []
                numero_linha = 0
                indice = 0
                indices_onde_a_linha_quebra = []
                for char in self._extrato:
                    indice += 1
                    if char == "\n":
                        indices_onde_a_linha_quebra.append(indice)
                        numero_linha += 1
                        for i in range(indices_onde_a_linha_quebra[indice-1],indices_onde_a_linha_quebra[indice]):
                            linhas_extrato[numero_linha].append(self._extrato[i])

                        substring = "Saque"
                        string = linhas_extrato[numero_linha]
                        isin = (substring in string)
                        if isin == True:
                            yield string

    def get_numero_depositos(self):
        return self._n_de_depositos
    
    def get_numero_saques(self):
        return self._n_de_saques
        