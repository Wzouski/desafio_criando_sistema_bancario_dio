menu = """

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "a":
        deposito = float(input("Informe o valor a ser depositado, e após, <ENTER>: "))

        if deposito >= 1:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou. O valor informado não é válido.")
        
    elif opcao == "b":
        saque = float(input("Informe o valor a ser sacado, e após, <ENTER>: "))
        saldo_insuficiente = saque > saldo
        saldo_fora_do_limite = saque > limite
        saques_diarios = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif saldo_fora_do_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif saques_diarios:
            print("Operação falhou! Número máximo de saques excedido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            print("Saque realizado com sucesso! Retire seu dinheiro.")
            numero_saques += 1
            

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "c":
        print("\n==============Extrato===============")
        print("Não foram realizadas operações nesta conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "d":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



