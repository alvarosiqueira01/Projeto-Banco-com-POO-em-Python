import cliente
from datetime import datetime
import time
import transacao
import os
from pathlib import Path


def log_operacao(func):

    def printa_operacao(*args):
        confirmacao = func(*args)

        if func.__name__ == "saque" or func.__name__ == "deposito":
            
            if confirmacao[0] == True:

                hora = datetime.now()
                c = args.__repr__()
                mensagem = f"\nOperação de {func.__name__} no valor de {confirmacao[1]} realizada em {hora} pelo cliente {c}."

                ROOT_PATH = Path(__file__).parent

                try:
                    with open(ROOT_PATH / "log.txt", "a") as log:
                        log.write(mensagem)
                except FileExistsError:
                    pass

        else:

            if confirmacao == True:

                hora = datetime.now()
                c = args.__repr__()
                mensagem = f"\nOperação de {func.__name__} realizada em {hora} pelo cliente {c}."

                ROOT_PATH = Path(__file__).parent

                try:
                    with open(ROOT_PATH / "log.txt", "x") as log:
                        log.write(mensagem)
                except FileExistsError:
                    pass
                finally:
                    with open(ROOT_PATH / "log.txt", "a") as log:
                        log.write(mensagem)
                        
        return confirmacao
    

    return printa_operacao




def criar_usuario(usuarios):

    print("\nPara criar o usuário, serão solicitados: nome, data de nascimento, CPF e endereço (formado por logradouro, número, bairro, cidade e estado.)")
    nome = input("Digite o nome do usuário: ")
    data = input("Digite a data de nascimento do usuário: ")
    cpf = input("Digite o CPF do usuário: ")

    for i in range(0,len(usuarios)):

        it = usuarios[i]
        if it[0].get_cpf() == cpf:

            print("\nErro: Já existe um usuário com este CPF.")
            return False
        

    logradouro = input("Digite o logradouro do usuário: ")
    numero = input("Digite o número do endereço usuário: ")
    bairro = input("Digite o bairro do usuário: ")
    cidade = input("Digite a cidade do usuário: ")
    estado = input("Digite a sigla do estado do usuário: ")
    endereco = logradouro + ", " + numero + " - " + bairro + " - " + cidade + "/" + estado

    senha = input("Defina uma senha para o cliente: ")
    senha_auth = input("Confirme a senha: ")

    if senha == senha_auth:

        cliente_login = cliente.PessoaFisica(nome, cpf, data, endereco)
        login = [cliente_login, senha]
        usuarios.append(login) 
        print("\nUsuário adicionado com sucesso!")
        return usuarios

    else:

        print("\nErro: as senhas digitadas diferem entre si. Tente novamente.")
        return False
    

@log_operacao
def deposito(usuario):

    print("\n==========Depósito==========")
    existe_conta = 0
    num_conta = int(input("Informe o número da conta a qual será feito o depósito: "))
    lista_contas_usuario = usuario.get_contas()

    for i in range(0,len(lista_contas_usuario)):

        obtem_conta = lista_contas_usuario[i]
        compara_nro = obtem_conta.get_numero()

        if compara_nro == num_conta:
            existe_conta = 1
            conta = lista_contas_usuario[i]
        
    if existe_conta == 0:
        print("\nErro: Não existe conta com o número fornecido.")
        print("==============================")
        return (False, -1)

    valor_deposito = float(input("Digite o valor do depósito: "))
    conta.depositar(valor_deposito)
    print("==============================")
    return (True, valor_deposito)


@log_operacao
def saque(usuario):

    print("\n==========Saque==========")  
    existe_conta = 0
    num_conta = int(input("Informe o número da conta da qual será feito o saque: "))
    lista_contas_usuario = usuario.get_contas()

    for i in range(0,len(lista_contas_usuario)):

        obtem_conta = lista_contas_usuario[i]
        compara_nro = obtem_conta.get_numero()

        if compara_nro == num_conta:
            existe_conta = 1
            conta = lista_contas_usuario[i]
        
    if existe_conta == 0:
        print("\nErro: Não existe conta com o número fornecido.")
        print("==============================")
        return (False, -1)

    valor_saque = float(input("Digite o valor do saque: "))
    conta.sacar(valor_saque)
    print("==============================")
    return (True, valor_saque)


@log_operacao
def extrato(usuario):

    print("\n==========Extrato==========")
    existe_conta = 0
    num_conta = int(input("Informe o número da conta: "))
    lista_contas_usuario = usuario.get_contas()

    for i in range(0,len(lista_contas_usuario)):

        obtem_conta = lista_contas_usuario[i]
        compara_nro = obtem_conta.get_numero()

        if compara_nro == num_conta:

            existe_conta = 1
            conta = lista_contas_usuario[i]
        
    if existe_conta == 0:

        print("\nErro: Não existe conta com o número fornecido.")
        print("==============================")
        return False

    else:
        
        menu = """

        Selecione quais operações deseja visualizar

        [d] Depósitos
        [s] Saques
        [t] Todas
        [v] Voltar

        => """

        while True:

            opcao = input(menu)

            if opcao == "d":
                t = transacao.Deposito()
                saldo = conta.get_saldo()
                print(f"Saldo atual da conta: R${saldo:.2f}.\nOperações anteriores:\n")
                print(conta.consultar_extrato(t))
                    
                print("==============================")
                return True
            
            elif opcao == "s":
                t = transacao.Saque()
                saldo = conta.get_saldo()
                print(f"Saldo atual da conta: R${saldo:.2f}.\nOperações anteriores:\n")
                print(conta.consultar_extrato(t))
                    
                print("==============================")
                return True
            
            elif opcao == "t":
                saldo = conta.get_saldo()
                print(f"Saldo atual da conta: R${saldo:.2f}.\nOperações anteriores:\n")
                print(conta.consultar_extrato())
                    
                    
                print("==============================")
                return True
            
            elif opcao == "v":
                return False

            else: 
                print("\nOperação inválida, por favor selecione novamente a operação desejada.") 


@log_operacao
def cadastrar_conta(usuario, numero_de_contas):

    print("\n")
    for i in range(0,3):

        print("Adicionando conta.")
        time.sleep(0.7)
        print("Adicionando conta..")
        time.sleep(0.7)
        print("Adicionando conta...")
        time.sleep(0.7)

    numero_de_contas = numero_de_contas + 1
    usuario.adicionar_conta(numero_de_contas)
    print("\nConta adicionada com sucesso! O número da conta é: ",numero_de_contas)
    cadastrar_conta.__name__ = "cadastro de conta"
    return True


class ContaIterador():

    def __init__(self, usuarios):
        self._index = 0 
        self._lista_de_usuarios = usuarios
        self._lista_de_contas = []

        self._num_contas = 0
        for i in range(0,len(usuarios)):
            
            for j in usuarios[i][0].get_contas():

                self._lista_de_contas.append([usuarios[i][0].get_cpf(),j])
                self._num_contas += 1

        self._lista_de_contas.append([None,None])

        


    def __iter__(self):
        return self
    

    def __next__(self):

        if self._lista_de_contas[self._index+1][0] != None:

            self._dados_da_conta_atual = [self._lista_de_contas[self._index][0], self._lista_de_contas[self._index][1].get_agencia(), self._lista_de_contas[self._index][1].get_numero()]
            

            mensagem = f"""

            Agência: {self._dados_da_conta_atual[1]}
            Número de conta: {self._dados_da_conta_atual[2]}
            Titular: {self._dados_da_conta_atual[0]}

            """

            self._index += 1
            return mensagem
    
        raise StopIteration
            

        
        








