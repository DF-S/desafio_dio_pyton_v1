menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print("Depósito")
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += (f"\n Depósito R$ {valor:.2f}")
            print(f"Depósito no valor de R$ {valor:.2f}, realizado com sucesso!")
        
        else:
            print("Valor invalido, tente novamente")
        
    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar!!!"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques > LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excedeu o limite diario.")
            
        elif excedeu_saque:
            print("Operação falhou! Número de saques execidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"\n Saque: R$ {valor:.2f}"
            numero_saques += 1
            print(f"Saque no valor de R$ {valor:.2f}, realizado com sucesso!2")
                
        
    elif opcao == "3":
        print("\n====================EXTRATO====================")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")
        
    elif opcao == "4":
        print("""
              ==========Obrigado por utilizar nossos terminais de Auto-Atendimento==========""")
        break
    
    else:
        print("Operação inválida, por favor selecione a operação desejada.")