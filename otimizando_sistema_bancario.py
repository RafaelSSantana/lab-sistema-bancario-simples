
def menu():
    print("""\n
    ----------- MENU -----------
    [1] Criar Usuário
        [a] Exibir usuarios
    [2] Abrir conta
        [b] Exibir contas
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [q] Sair


    => """)
    return input()


def deposito (saldo, extrato, /): #Deposito
    print("\nDepósito\n--------------------------------------")
    valor_deposito = float(input("Insira o valor do depósito: "))
    print("") #Pula linha

    if valor_deposito > 0: #Deposito concluído
        saldo += valor_deposito
        extrato += f"Depósito : R$ {valor_deposito:.2f}\n"
        print(f"Concluído com sucesso o depósito de R$ {valor_deposito:.2f}\n--------------------------------------")
    else:
        print("Não foi possível concluir a operação, pois o valor inserido é inválido.")
    
    return saldo, extrato


def saque (*, saldo, extrato, numero_saques, limite_saques): #Saque
    limite = 500

    print("\nSaque\n--------------------------------------")
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    print("") #Pula Linha

    fim_num_saques = numero_saques >= limite_saques
    invalido_ou_semlimite = valor_saque <= 0 or valor_saque >= limite
    saldo_insuficiente = valor_saque > saldo

    if fim_num_saques:
        print("Não foi possível concluir a operação, pois seu limite diário de saques já foi atingido\n--------------------------------------")

    elif invalido_ou_semlimite:
        print("Não foi possível concluir a operação, pois o valor inserido é inválido, ou acima do seu limite de saque atual\n--------------------------------------")

    elif saldo_insuficiente: 
        print("Não foi possível concluir a operação, pois você não possui saldo o suficiente\n--------------------------------------")

    else: #Saque concluído
        numero_saques = numero_saques + 1
        saldo -= valor_saque
        extrato += f"Saque : R$ {valor_saque:.2f}\n"
        print(f"Concluído com sucesso o saque de R$ {valor_saque:.2f}\n--------------------------------------")
        print(f"saques restantes : {numero_saques}")
    
    return saldo, extrato, numero_saques


def exibir_extrato (saldo, /, *, extrato): #Extrato
    print("\nExtrato\n-------------------Extrato-------------------")

    if extrato != "":
        print(extrato,f"\nSaldo Atual: R$ {saldo:.2f}\n---------------------------------------------")
    else:
        print("Não foram realizadas movimentações.\n---------------------------------------------")


def criar_usuario(usuario):
    cpf = input("Insira seu CPF (apenas os números): ")
    usuario_existe = busca_usuario(usuario, cpf)

    if usuario_existe:
        print(20*"=")
        print("cpf já cadastrado")
        print(20*"=")

    else:
        #
        print("Preencha os campos para completar o seu cadastro:\n")
        
        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento (dd-mm-aa): ")
        endereco = input("endereço (logradouro, nr - bairro - cidade / sigla estado): ")
        #       
        usuario.append({"nome" : nome, "cpf" : cpf, "nascimento" : nascimento, "endereço" : endereco})

        print(20*"=")
        print("cadastro bem sucedido!")
        print(20*"=")


def busca_usuario(usuarios, cpf):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuario_encontrado[0] if usuario_encontrado else None


def criar_conta(usuario, conta, num_conta):
    AGENCIA = "0001"
    cpf = input("Insira seu CPF: ")
    usuario_cadastrado = busca_usuario(usuario, cpf)

    if usuario_cadastrado:
        num_conta += 1
        conta.append({"agencia" : AGENCIA, "numero da conta" : num_conta, "usuario" : usuario_cadastrado})

        print(20*"=")
        print("conta criada com sucesso!")
        print(20*"=")

        return num_conta

    else:
        print(30*"=")
        print("nenhuma conta vinculada ao cpf")
        print(30*"=")


def main():
    ##
    saldo = 0
    extrato = ""
    numero_saques = 0
    numero_conta = 0
    lista_usuarios = []
    lista_contas = []
    LIMITE_SAQUES = 3
    ##

    while True:
        opcao = menu()

        if opcao == "1": # criar usuario
            criar_usuario(lista_usuarios)      

        elif opcao == "a": # exibir usuarios
            print(lista_usuarios)

        elif opcao == "2": # abrir conta
            numero_conta = criar_conta(lista_usuarios, lista_contas, numero_conta)  

        elif opcao == "b": # exibir contas
            print(lista_contas)

        elif opcao == "3": # deposito
            saldo, extrato = deposito(saldo, extrato)

        elif opcao == "4": # saque
            saldo, extrato, numero_saques = saque(saldo = saldo, extrato = extrato, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

        elif opcao == "5": # extrato
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "q": # encerrar execução
            break

        else: #entrada inválida
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()