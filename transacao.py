from abc import ABC
import conta
from datetime import datetime
from datetime import date

LIMITE_SAQUES = 3

LIMITE_TRANSACOES = 10


class Transacao(ABC):
    def registrar(self, conta):
        conta.get_historico().adicionar_transacao(self)


class Deposito(Transacao):

    def __init__(self):
        self._valor = 0.0
        self._dia = date.today()

    def validar(self, conta, valor, dia_transacao_anterior):

        if dia_transacao_anterior == self._dia:
            qtd_transacoes = conta.get_qtd_transacoes()
            conta.set_qtd_transacoes(qtd_transacoes+1)
            
            if conta.get_qtd_transacoes() > LIMITE_TRANSACOES:
                print("Erro: número de transações diário excedido.")
                return False
            
        else:
            conta.set_qtd_transacoes(0)

        self._conta = conta
        self._valor = valor
        if valor < 0:
            print("Impossível fazer depósito negativo.")
            return False
        else: 
            print("Depósito realizado com sucesso.")
            self._data_e_hora = datetime.now()
            return True
            
    def get_valor(self):
        return self._valor
    
    def get_data_e_hora(self):
        return self._data_e_hora
    
    def get_dia(self):
        return self._dia
    


class Saque(Transacao):

    def __init__(self):
        self._valor = 0.0
        self._dia = date.today()
        
    def validar(self, conta, valor, dia_transacao_anterior):

        if dia_transacao_anterior == self._dia:
            qtd_transacoes = conta.get_qtd_transacoes()
            conta.set_qtd_transacoes(qtd_transacoes+1)
            
            if conta.get_qtd_transacoes() > LIMITE_TRANSACOES:
                print("Erro: número de transações diário excedido.")
                return False
            
        else:
            conta.set_qtd_transacoes(0)

        self._conta = conta
        self._valor = valor
        if conta.get_qtd_saques() > LIMITE_SAQUES:
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
                x = conta.get_qtd_saques() + 1
                conta.set_qtd_saques(x)
                print("Saque realizado com sucesso.")
                self._data_e_hora = datetime.now()
                return True
        
    def get_valor(self):
        return self._valor
    
    def get_data_e_hora(self):
        return self._data_e_hora
    
    def get_dia(self):
        return self._dia


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
            
            numero_linha = 0
            indice = 0
            indices_onde_a_linha_quebra = []
            indices_onde_a_linha_quebra.append(0)
            linhas_extrato = []
            for char in self._extrato:
                indice += 1
                if char == "\n":
                    indices_onde_a_linha_quebra.append(indice)
                    numero_linha += 1
                    linha_atual = ""
                
                    for i in range(indices_onde_a_linha_quebra[numero_linha-1],indices_onde_a_linha_quebra[numero_linha]):
                        linha_atual = linha_atual + self._extrato[i]

                    linhas_extrato.append(linha_atual)

            for i in linhas_extrato: 
                yield i

        else: 

            if isinstance(transacao, Deposito):

                numero_linha = 0
                indice = 0
                indices_onde_a_linha_quebra = []
                indices_onde_a_linha_quebra.append(0)
                linhas_extrato = []
                for char in self._extrato:
                    indice += 1
                    if char == "\n":
                        indices_onde_a_linha_quebra.append(indice)
                        numero_linha += 1
                        linha_atual = ""
                    
                        for i in range(indices_onde_a_linha_quebra[numero_linha-1],indices_onde_a_linha_quebra[numero_linha]):
                            linha_atual = linha_atual + self._extrato[i]

                        substring = "Depósito"
                        string = linha_atual
                        isin = (substring in string)
                        if isin == True:
                            linhas_extrato.append(linha_atual)

                for i in linhas_extrato: 
                    yield i

            if isinstance(transacao, Saque):

                numero_linha = 0
                indice = 0
                indices_onde_a_linha_quebra = []
                indices_onde_a_linha_quebra.append(0)
                linhas_extrato = []
                for char in self._extrato:
                    indice += 1
                    if char == "\n":
                        indices_onde_a_linha_quebra.append(indice)
                        numero_linha += 1
                        linha_atual = ""
                    
                        for i in range(indices_onde_a_linha_quebra[numero_linha-1],indices_onde_a_linha_quebra[numero_linha]):
                            linha_atual = linha_atual + self._extrato[i]

                        substring = "Saque"
                        string = linha_atual
                        isin = (substring in string)
                        if isin == True:
                            linhas_extrato.append(linha_atual)

                for i in linhas_extrato: 
                    yield i

    def get_numero_depositos(self):
        return self._n_de_depositos
    
    def get_numero_saques(self):
        return self._n_de_saques
    

        


