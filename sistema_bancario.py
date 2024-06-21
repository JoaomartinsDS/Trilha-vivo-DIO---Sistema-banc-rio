menu = """
    Bem vindo! Selecione a opção desejada:
    1 - depósito
    2 - saque
    3 - extrato
    4 - sair
    5 - criar usuário
    6 - criar conta
    7 - listar contas

"""
exibir_menu = True
saldo = 0
valor_deposito = 0
LIMITE_QTD_SAQUE_DIARIO = 3
VALOR_LIMITE_SAQUE = 500
saques_realizados = 0
extrato = ""
usuarios = []
contas = []

def saque(*,saldo,valor,extrato,VALOR_LIMITE_SAQUE,LIMITE_QTD_SAQUE_DIARIO,saques_realizados):
    if saques_realizados < LIMITE_QTD_SAQUE_DIARIO:
            if valor_saque <= VALOR_LIMITE_SAQUE:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"\nSaque: R${valor_saque:.2f}"
                    print("Saque realizado com sucesso!")
                    saques_realizados += 1
                else:
                    print("Não é possível realizar o saque! saldo insuficiente.")
            else:
                print("O valor de saque excede o valor permitido de R$ 500,00 ao dia.")
            
    else:
        print("Quantidade de saque diário excedida.")
    return saldo,extrato,saques_realizados

def deposito(saldo,valor,extrato):
    if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R${valor:.2f}"
            print("Depósito realizado com sucesso!")
    else:
            print("valor de depósito inválido.")
    return saldo,extrato
 
def exibir_extrato(saldo,/,*,extrato):
    print("\n=========== EXTRATO ===========")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\n\nSaldo disponível {saldo:.2f}")
    print("\n===============================")
    
def criar_usuario(usuarios,filtrar_cpf_cadastrado):
    cpf = input("Digite seu CPF: ")
    tem_cpf = filtrar_cpf_cadastrado(cpf,usuarios)
    if tem_cpf:
        print("Usuário já cadastrado!")
    else:
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        endereco = input("Digite seu endereço: ")
        usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco,"cpf":cpf})
        print("Usuário cadastrado com sucesso!")
        return usuarios

def filtrar_cpf_cadastrado(cpf,usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else {}
def criar_conta(usuarios,filtrar_cpf_cadastrado,contas):
    cpf = input("Digite seu cpf: ")
    usuario_filtrado = filtrar_cpf_cadastrado(cpf,usuarios)
    if usuario_filtrado:
        contas.append({"conta":len(contas)+1,"agencia":1,"usuario":usuario_filtrado})
    else:
        print("usuário não encontrado.")
    return contas
def listar_contas(contas):
    for conta in contas:
        print(f"""
              =========== Contas ===========
              
              Agência: {conta["agencia"]}"
              Conta: {conta["conta"]}
              Titular: {conta["usuario"]["nome"]}
              
              ==============================""")
              
    
    
 
while exibir_menu == True:
    print(menu)
    opcao = int(input(""))
    if opcao == 1:
        valor = int(input("Informe o valor de depósito: "))
        saldo,extrato = deposito(saldo,valor,extrato)

    if opcao == 2:
        valor_saque = int(input("Digite o valor a ser sacado: "))
        saldo,extrato,saques_realizados = saque(saldo=saldo,valor=valor_saque,extrato=extrato,VALOR_LIMITE_SAQUE=VALOR_LIMITE_SAQUE,LIMITE_QTD_SAQUE_DIARIO=LIMITE_QTD_SAQUE_DIARIO,saques_realizados=saques_realizados)
    if opcao == 3:
        exibir_extrato(saldo,extrato=extrato)
    if opcao == 4:
        exibir_menu = False
    if opcao == 5:
        criar_usuario(usuarios,filtrar_cpf_cadastrado)
        print(usuarios)
    if opcao == 6:
        contas = criar_conta(usuarios,filtrar_cpf_cadastrado,contas)
        print(contas)
    if opcao == 7:
        listar_contas(contas)
        
        
        
print("Obrigado por usar nosso sistema!")
        
    