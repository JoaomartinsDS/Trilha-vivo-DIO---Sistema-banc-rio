menu = """
    Bem vindo! Selecione a opção desejada:
    1 - depósito
    2 - saque
    3 - extrato
    4 - sair

"""
exibir_menu = True
saldo = 0
valor_deposito = 0
LIMITE_QTD_SAQUE_DIARIO = 3
VALOR_LIMITE_SAQUE = 500
saques_realizados = 0
extrato = """
Extrato:
    
"""
while exibir_menu == True:
    print(menu)
    opcao = int(input(""))
    if opcao == 1:
        valor_deposito = int(input("Informe o valor de depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\nDepósito: R${valor_deposito:.2f}"
            print("Depósito realizado com sucesso!")
        else:
            print("valor de depósito inválido.")
    if opcao == 2:
        if saques_realizados < LIMITE_QTD_SAQUE_DIARIO:
            valor_saque = int(input("Digite o valor a ser sacado: "))
            if valor_saque <= VALOR_LIMITE_SAQUE:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"\nSaque: R${valor_saque:.2f}"
                    print("Saque realizado com sucesso!")
                else:
                    print("Não é possível realizar o saque! saldo insuficiente.")
            else:
                print("O valor de saque excede o valor permitido de R$ 500,00 ao dia.")
            
        else:
            print("Quantidade de saque diário excedida.")
    if opcao == 3:
        print(extrato)
        print(f"\n\nSaldo disponível {saldo:.2f}")
    if opcao == 4:
        exibir_menu = False
print("Obrigado por usar nosso sistema!")
        
    