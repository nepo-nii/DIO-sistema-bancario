menu = '''
[d] = deposito
[s] = saque 
[e] = extrato
[q] = sair
'''

###constantes e valores limites
limite_saques = 3
saldo = 0
extrato = ""
numero_saques = 0
limite = 500

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor>0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Voce não tem saldo suficiente.")
        elif excedeu_limite:
            print("operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("operação falhou! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == "e":
        print("\n ===== EXTRATO =====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
    elif opcao == "q":
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')