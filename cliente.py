import transacao
import conta

class Cliente():
    _contas = []
    
    def realizar_transacao(self, conta, transacao):
        for i in self._contas:
            if self._contas[i] == conta:
                valor = float(input("Informe o valor da transação: "))
                if isinstance(transacao, transacao.Deposito()) == True:
                    conta.depositar(valor)
                if isinstance(transacao, transacao.Saque()) is True:
                    conta.sacar(valor)

    def adicionar_conta(self, numero):
        existe = False
        for i in range(0,len(self._contas)):
            if self._contas[i].get_numero() == numero:
                existe = True
        if existe == True:
            print("Erro: Já existe uma conta cadastrada com esse número.")
        else:
            conta_nova = conta.ContaCorrente(self, numero)
            self._contas.append(conta_nova)

    def get_contas(self):
        return self._contas

    
        

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._endereco = endereco
        self._contas = []

    def get_cpf(self):
        return self._cpf
    
    def get_contas(self):
        return self._contas
    
    


        
            


    
        
        