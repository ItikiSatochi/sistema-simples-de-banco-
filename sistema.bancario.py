menu = """
[4] Usuário 
[3] Depositar 
[2] Sacar
[1] Extrato
[0] Sair

=>"""

saldo = 0
limite = 600

extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operção Falhou! O valor informado é invalido. ")

    elif opcao == "2":
        valor = float(input("Informe o valor do Saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > saldo 

        excedeu_saque = numero_saque = LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excedeu o limite.")

        elif excedeu_saque:
            print("Operação Falhou! Número máximo de saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1 

        else:
            print("Operação Falhou! O valor informado é invalido.")
        
         
    elif opcao == "3":

      print("\n================EXTRATO================")
      print("Não foram realizada movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("=============================================")


    elif opcao == "0":
        break

    
    else:
        print("Operação Invalida, por favor selecione novamente a operação desejada.")
  





