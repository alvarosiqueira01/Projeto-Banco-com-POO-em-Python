import cliente
import transacao
from datetime import date
from datetime import timedelta


class Conta():
    
    def get_saldo(self):
        return self._saldo
    
    def get_numero(self):
        return self._numero
    
    def get_agencia(self):
        return self._agencia
    
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero
        self._saldo = 0.0
        historico = transacao.Historico()
        self._historico = historico
        self._agencia = '0001'

        um_dia = timedelta(days=1)
        hoje = date.today()
        ontem = hoje - um_dia
        self._dia_transacao_anterior = ontem #valor default para quando conta é criada, como se fosse -1


    def sacar(self, valor):
        inicia_transacao = transacao.Saque()
        saque = inicia_transacao.validar(self, valor, self._dia_transacao_anterior)
        if saque == True:
            self._saldo = self._saldo - valor 
            inicia_transacao.registrar(self)
            self._dia_transacao_anterior = inicia_transacao.get_dia()
            return True
        else:
            return False


    def depositar(self, valor):
        inicia_transacao = transacao.Deposito()
        deposito = inicia_transacao.validar(self, valor, self._dia_transacao_anterior)
        if deposito == True:
            self._saldo = self._saldo + valor 
            inicia_transacao.registrar(self)
            self._dia_transacao_anterior = inicia_transacao.get_dia()
            return True
        else:
            return False
        
    def consultar_extrato(self, tr=None):

        extrato_solicitado = []
        mensagem = ""
        if not tr:
            gerador = self._historico.gerar_relatorio(tr)
            for i in range(0,self._historico.get_numero_saques()+self._historico.get_numero_depositos()):

                extrato_solicitado.append(next(gerador))
            
            for i in extrato_solicitado:
                mensagem = mensagem + i

            return mensagem
                    
        if isinstance(tr, transacao.Saque):
            gerador = self._historico.gerar_relatorio(tr)
            for i in range(0,self._historico.get_numero_saques()):
                        
                extrato_solicitado.append(next(gerador))
            
            for i in extrato_solicitado:
                mensagem = mensagem + i

            return mensagem
            
        if isinstance(tr, transacao.Deposito):
            gerador = self._historico.gerar_relatorio(tr)
            for i in range(0,self._historico.get_numero_depositos()):
                        
                extrato_solicitado.append(next(gerador))
            
            for i in extrato_solicitado:
                mensagem = mensagem + i

            return mensagem
    

    def get_historico(self):
        return self._historico
        

class ContaCorrente(Conta):
    _limite = 500
    _qtd_saques_diaria = 0
    _qtd_transacoes_diaria = 0

    def get_limite(self):
        return self._limite
    
    def set_limite(self, limite):
        self._limite = limite

    def get_qtd_saques(self):
        return self._qtd_saques_diaria
    
    def set_qtd_saques(self, qtd_saques):
        self._qtd_saques_diaria = qtd_saques

    def get_qtd_transacoes(self):
        return self._qtd_transacoes_diaria
    
    def set_qtd_transacoes(self, qtd_transacoes):
        self._qtd_transacoes_diaria = qtd_transacoes