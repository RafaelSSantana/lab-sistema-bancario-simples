

menu = """\n
Menu:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\nDepósito\n--------------------------------------")
        #Deposito
            #Deve ser possível depositar valores positivos
            #Não precisa identificar cliente pois só há 1
            #Depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
        valor_deposito = float(input("Insira o valor do depósito: "))
        print("") #Pula linha

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito : R$ {valor_deposito:.2f}\n"
            print(f"Concluído com sucesso o depósito de R$ {valor_deposito:.2f}\n--------------------------------------")
        else:
            print("Não foi possível concluir a operação, pois o valor inserido é inválido.")

    elif opcao == "s":
        print("\nSaque\n--------------------------------------")
        #Saque
            #Deve permitir 3 saques diários com limite de 500,00 por saque
            #Caso não tenha saldo em conta, o sistema deve exibir mensagem informando que não será possível sacar o dinheiro por falta de saldo
            #Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        print("") #Pula Linha

        if numero_saques >= LIMITE_SAQUES:
            print("Não foi possível concluir a operação, pois seu limite diário de saques já foi atingido\n--------------------------------------")

        elif valor_saque <= 0 or valor_saque >= limite:
            print("Não foi possível concluir a operação, pois o valor inserido é inválido, ou acima do seu limite de saque atual\n--------------------------------------")

        elif valor_saque > saldo: 
            print("Não foi possível concluir a operação, pois você não possui saldo o suficiente\n--------------------------------------")

        else: #Saque concluído
            numero_saques += 1
            saldo -= valor_saque
            extrato += f"Saque : R$ {valor_saque:.2f}\n"
            print(f"Concluído com sucesso o saque de R$ {valor_saque:.2f}\n--------------------------------------")

    elif opcao == "e":
        print("\nExtrato\n-------------------Extrato-------------------")
        #Extrato
            #Deve listar todos os depósitos e saques realizados na conta
            #No fim da listagem deve exibir o saldo atual
            #O formato deve ser R$ 1500.00
        if extrato != "":
            print(extrato,f"\nSaldo Atual: R$ {saldo:.2f}\n---------------------------------------------")
        else:
            print("Não foram realizadas movimentações.\n---------------------------------------------")
            
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")