import operacoes


usuarios = []

numero_de_contas = 0

menu_inicial = """

Selecione a opção que deseja:

[l] Fazer login de cliente
[cc] Cadastrar cliente
[lc] Listar Contas
[q] Sair

=> """


menu = """

[d] Realizar depósito
[s] Realizar saque
[e] Consultar Extrato
[cc] Cadastrar conta
[v] Voltar

=> """



while True: 

        opcao_menu_ini = input(menu_inicial)

        if opcao_menu_ini == "l":

            usuario_login = input("Digite o CPF: ")
            existe_usuario = False

            for i in range(0,len(usuarios)):

                it_cpf = usuarios[i][0]

                if it_cpf.get_cpf() == usuario_login:

                    existe_usuario = True
                    senha_login = input("Digite a senha: ")
                    it_senha = usuarios[i][1]

                    if senha_login == it_senha:

                        print("\n\nBem vindo ao banco! Selecione a operação que deseja realizar:")

                        while True: 

                            opcao = input(menu)

                            if opcao == "d":

                                depositou = operacoes.log_operacao(operacoes.deposito(it_cpf))
                                if depositou == False:
                                    break

                            elif opcao == "s":    

                                sacou = operacoes.log_operacao(operacoes.saque(it_cpf))
                                if depositou == False:
                                    break
                                

                            elif opcao == "e":

                                tirou_extrato = operacoes.log_operacao(operacoes.extrato(it_cpf))
                                if tirou_extrato == False:
                                    break
                                

                            elif opcao == "cc":
                                
                                cadastrou = operacoes.log_operacao(operacoes.cadastrar_conta(it_cpf, numero_de_contas))
                                if cadastrou == False:
                                    break
                                else: 
                                    numero_de_contas += 1
                                

                            elif opcao == "v":
                                break

                            else: 
                                print("\nOperação inválida, por favor selecione novamente a operação desejada.") 


                    else: 
                        
                        print("Senha errada. Tente novamente.")
                        break  
                
            if existe_usuario == False:

                print("Erro: Não há cadastrado cliente com tal CPF. Tente novamente.")  
                break
                    
                        

        elif opcao_menu_ini == "cc":    

            criou = operacoes.criar_usuario(usuarios)
            if criou == False:
                break
            else:
                usuarios = criou


        elif opcao_menu_ini == "lc":    

            existe_conta = False
            for i in range(0,len(usuarios)):
                it = usuarios[i][0]
                if len(it.get_contas()) > 0:
                    existe_conta = True

            if existe_conta:

                for dados in operacoes.ContaIterador(usuarios):
                    print(dados)

            else:

                print("\nErro: Não há contas cadastradas.")
                break
            
            
        elif opcao_menu_ini == "q":
            break

        else: 
            print("Operação inválida, por favor selecione novamente a operação desejada.")        


