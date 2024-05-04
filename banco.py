import cliente 


usuarios = []

numero_de_contas = 0

menu_inicial = """

Selecione a opção que deseja:

[l] Fazer login de cliente
[cc] Cadastrar cliente
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

                                print("\nDepósito")
                                existe_conta = 0
                                num_conta = int(input("Informe o número da conta a qual será feito o depósito: "))
                                lista_contas_it = it_cpf.get_contas()

                                for i in range(0,len(lista_contas_it)):

                                    obtem_conta = lista_contas_it[i]
                                    compara_nro = obtem_conta.get_numero()

                                    if compara_nro == num_conta:
                                        existe_conta = 1
                                        conta = lista_contas_it[i]
                                    
                                if existe_conta == 0:
                                    print("Erro: Não existe conta com o número fornecido.")
                                    break

                                valor_deposito = float(input("Digite o valor do depósito: "))
                                conta.depositar(valor_deposito)

                            elif opcao == "s":    

                                print("\nSaque")  
                                existe_conta = 0
                                num_conta = int(input("Informe o número da conta da qual será feito o saque: "))
                                lista_contas_it = it_cpf.get_contas()

                                for i in range(0,len(lista_contas_it)):

                                    obtem_conta = lista_contas_it[i]
                                    compara_nro = obtem_conta.get_numero()

                                    if compara_nro == num_conta:
                                        existe_conta = 1
                                        conta = lista_contas_it[i]
                                    
                                if existe_conta == 0:
                                    print("Erro: Não existe conta com o número fornecido.")
                                    break

                                valor_saque = float(input("Digite o valor do saque: "))
                                conta.sacar(valor_saque)

                            elif opcao == "e":

                                print("\nExtrato")
                                existe_conta = 0
                                num_conta = int(input("Informe o número da conta: "))
                                lista_contas_it = it_cpf.get_contas()

                                for i in range(0,len(lista_contas_it)):

                                    obtem_conta = lista_contas_it[i]
                                    compara_nro = obtem_conta.get_numero()

                                    if compara_nro == num_conta:

                                        existe_conta = 1
                                        conta = lista_contas_it[i]
                                    
                                if existe_conta == 0:

                                    print("Erro: Não existe conta com o número fornecido.")
                                    break

                                print(conta.consultar_extrato())


                            elif opcao == "cc":
                                
                                numero_de_contas = numero_de_contas + 1
                                it_cpf.adicionar_conta(numero_de_contas)
                                print("Conta adicionada com sucesso! O número da conta é: ", numero_de_contas)


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
            
            print("Para criar o usuário, serão solicitados: nome, data de nascimento, CPF e endereço (formado por logradouro, número, bairro, cidade e estado.)")
            nome = input("Digite o nome do usuário: ")
            data = input("Digite a data de nascimento do usuário: ")
            cpf = input("Digite o CPF do usuário: ")

            for i in range(0,len(usuarios)):

                it = usuarios[i]
                if it[0].get_cpf() == cpf:

                    print("Erro: Já existe um usuário com este CPF.")
                    break
                

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
                print("Usuário adicionado com sucesso!")

            else:

                print("Erro: as senhas digitadas diferem entre si. Tente novamente.")
                break
            


        elif opcao_menu_ini == "q":
            break

        else: 
            print("Operação inválida, por favor selecione novamente a operação desejada.")        


    